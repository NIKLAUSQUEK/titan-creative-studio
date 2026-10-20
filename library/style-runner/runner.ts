// titan-os / style-runner — Railway Function (Bun). Builds the creator Style DNA library from vidIQ.
// Cron "1 12 * * *" UTC (= 20:01 Asia/Singapore). Exits immediately outside the 20:xx SGT hour unless FORCE_RUN=1, so deploys/variable changes never fire it early. One due batch per run. Hard credit guards.
// Env (reference vars from `workers`): SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, OPENROUTER_API_KEY, TELEGRAM_BOT_TOKEN
// Env (new, set by Klaus): VIDIQ_API_KEY.  Optional: TELEGRAM_CHAT_ID, LLM_MODEL.

const SUPA = Bun.env.SUPABASE_URL!, SKEY = Bun.env.SUPABASE_SERVICE_ROLE_KEY!;
const VIDIQ_URL = "https://mcp.vidiq.com/mcp";
const MODEL = Bun.env.LLM_MODEL || "anthropic/claude-sonnet-4.5";
const COST = { short: 10, long: 25 };
const EXTRACT = `Break this video down for a style library. Use these headings: HOOK (first 2 seconds: what is seen, heard, written); STRUCTURE (beats with timestamps); PACING (average shot length, number of cuts, jump cuts, pauses removed or kept); CAMERA (who holds it, angle, shot sizes, movement, POV); LIGHTING & GRADE (key light quality, colour temperature, contrast, saturation); CAPTIONS & TEXT (font style, position, animation, word-by-word or static, emoji use); SOUND (music genre/energy, SFX types and where they hit, voice processing); VOICE & DELIVERY (speed, rhythm, accent, energy, persona); EDIT EFFECTS (zooms, transitions, shakes, freezes, overlays, memes); PEOPLE & SETTING; TARGET AUDIENCE (likely age band and who it is for, and why); SIGNATURE MOVE. Describe only what is on screen.`;

// ---------- Supabase REST ----------
async function db(path: string, init: RequestInit = {}) {
  const r = await fetch(`${SUPA}/rest/v1/${path}`, { ...init, headers: { apikey: SKEY, Authorization: `Bearer ${SKEY}`, "Content-Type": "application/json", Prefer: "return=representation", ...(init.headers || {}) } });
  const t = await r.text(); if (!r.ok) throw new Error(`DB ${path} ${r.status}: ${t.slice(0, 300)}`);
  return t ? JSON.parse(t) : null;
}
const patch = (table: string, q: string, body: any) => db(`${table}?${q}`, { method: "PATCH", body: JSON.stringify(body) });
const insert = (table: string, body: any) => db(table, { method: "POST", body: JSON.stringify(body) });
async function log(batch: number | null, level: string, message: string, credits = 0) { console.log(`[${level}] b${batch} ${message}`); try { await insert("style_run_log", { batch, level, message, credits }); } catch (e) { console.error(e); } }
async function notify(text: string) {
  const tok = Bun.env.TELEGRAM_BOT_TOKEN, chat = Bun.env.TELEGRAM_CHAT_ID; if (!tok || !chat) return;
  await fetch(`https://api.telegram.org/bot${tok}/sendMessage`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ chat_id: chat, text }) }).catch(() => {});
}

// ---------- Minimal MCP (Streamable HTTP) client ----------
let sid: string | null = null, rid = 0;
async function rpc(method: string, params: any, notification = false) {
  const body: any = notification ? { jsonrpc: "2.0", method, params } : { jsonrpc: "2.0", id: ++rid, method, params };
  const r = await fetch(VIDIQ_URL, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json, text/event-stream", Authorization: `Bearer ${Bun.env.VIDIQ_API_KEY}`, "MCP-Protocol-Version": "2025-06-18", ...(sid ? { "Mcp-Session-Id": sid } : {}) }, body: JSON.stringify(body) });
  const s = r.headers.get("mcp-session-id"); if (s) sid = s;
  if (notification) return null;
  const text = await r.text(); let msg: any = null;
  if ((r.headers.get("content-type") || "").includes("text/event-stream")) {
    for (const line of text.split("\n")) if (line.startsWith("data:")) { try { const j = JSON.parse(line.slice(5).trim()); if (j.id === body.id) msg = j; } catch {} }
  } else { try { msg = JSON.parse(text); } catch {} }
  if (!msg) throw new Error(`MCP ${method} HTTP ${r.status}: ${text.slice(0, 300)}`);
  if (msg.error) throw new Error(`MCP ${method}: ${JSON.stringify(msg.error)}`);
  return msg.result;
}
async function tool(name: string, args: any) {
  const res = await rpc("tools/call", { name, arguments: args });
  const text = (res?.content || []).filter((c: any) => c.type === "text").map((c: any) => c.text).join("\n");
  if (res?.isError) throw new Error(`${name}: ${text.slice(0, 300)}`);
  let data: any = res?.structuredContent; if (!data) { try { data = JSON.parse(text); } catch { data = {}; } }
  return { text, data };
}
const pick = (o: any, keys: string[], text = ""): any => { for (const k of keys) if (o && o[k] != null) return o[k]; for (const k of keys) { const m = text.match(new RegExp(`"?${k}"?\\s*[:=]\\s*"?([\\w.-]+)`)); if (m) return m[1]; } return undefined; };

// ---------- LLM (OpenRouter) ----------
async function llm(prompt: string, web = false) {
  const body: any = { model: MODEL, messages: [{ role: "user", content: prompt }] };
  if (web) body.plugins = [{ id: "web", max_results: 8 }];
  const r = await fetch("https://openrouter.ai/api/v1/chat/completions", { method: "POST", headers: { Authorization: `Bearer ${Bun.env.OPENROUTER_API_KEY}`, "Content-Type": "application/json" }, body: JSON.stringify(body) });
  const j: any = await r.json(); if (!r.ok) throw new Error(`LLM ${r.status}: ${JSON.stringify(j).slice(0, 300)}`);
  return j.choices?.[0]?.message?.content || "";
}
const SHORT_RE = /^https:\/\/(www\.)?(tiktok\.com\/@[\w.]+\/video\/\d+|instagram\.com\/(reel|p)\/[\w-]+\/?|youtube\.com\/shorts\/[\w-]{11})/;
const LONG_RE = /^https:\/\/(www\.)?(youtube\.com\/watch\?v=[\w-]{11}|youtu\.be\/[\w-]{11})/;
async function findUrls(name: string, category: string, n: number, longForm: boolean) {
  const kind = longForm ? "long-form YouTube brand films/commercials (youtube.com/watch?v= URLs)" : "short-form videos (TikTok, Instagram Reels, or YouTube Shorts)";
  const out = await llm(`Find ${n} of the most-viewed, representative ${kind} by "${name}" (category: ${category}), preferring the last 12 months. Formats: TikTok https://www.tiktok.com/@handle/video/<digits> (never vm.tiktok or /t/ short links); Instagram https://www.instagram.com/reel/<code>/; YouTube Shorts https://www.youtube.com/shorts/<id>; long-form https://www.youtube.com/watch?v=<id>. ONLY include URLs you actually saw in search results. Reply with ONLY JSON: {"urls":["..."]}`, true);
  const m = out.match(/\{[\s\S]*\}/); let urls: string[] = [];
  try { urls = JSON.parse(m ? m[0] : "{}").urls || []; } catch {}
  const re = longForm ? LONG_RE : SHORT_RE;
  return [...new Set(urls.map((u) => u.trim()).filter((u) => re.test(u)))].slice(0, n);
}

// ---------- Main ----------
const sgNow = new Date(Date.now() + 8 * 3600e3);
const sgToday = sgNow.toISOString().slice(0, 10);
if (sgNow.getUTCHours() !== 20 && Bun.env.FORCE_RUN !== "1") { console.log(`Outside 20:00-20:59 SGT (now ${sgNow.toISOString().slice(11, 16)} SGT); exiting without work.`); process.exit(0); }
const settings = Object.fromEntries((await db("style_settings?select=key,value")).map((r: any) => [r.key, r.value]));
const BUFFER = +settings.buffer_credits || 270, TOTAL_CAP = +settings.total_spend_cap || 1730, PER = +settings.videos_per_creator || 4;
const batches = await db(`style_batches?select=*&status=neq.done&run_date=lte.${sgToday}&order=batch.asc&limit=1`);
if (!batches.length) { await log(null, "info", `No batch due on ${sgToday}`); process.exit(0); }
const B = batches[0];
if (B.batch > 1 && settings.pilot_approved !== "true") { await log(B.batch, "wait", "Waiting for pilot approval (style_settings.pilot_approved=true)"); await notify(`Style runner: batch ${B.batch} is due but waiting for PILOT APPROVED.`); process.exit(0); }
if (!Bun.env.VIDIQ_API_KEY) { await log(B.batch, "blocked", "VIDIQ_API_KEY not set"); process.exit(0); }

await rpc("initialize", { protocolVersion: "2025-06-18", capabilities: {}, clientInfo: { name: "titan-style-runner", version: "1.0" } });
await rpc("notifications/initialized", {}, true);
const bal = await tool("vidiq_balance", {});
const balance = +pick(bal.data, ["totalCredits"], bal.text);
const totalSpent = (await db("style_batches?select=credits_spent")).reduce((a: number, r: any) => a + r.credits_spent, 0);
let batchSpent = B.credits_spent;
const batchLeft = B.credit_cap - batchSpent;
if (!(balance - batchLeft >= BUFFER)) { await log(B.batch, "blocked", `Balance ${balance} would breach ${BUFFER} buffer (batch needs ${batchLeft})`); await notify(`Style runner BLOCKED: balance ${balance}, batch ${B.batch} needs ${batchLeft}, buffer ${BUFFER}.`); process.exit(0); }
await patch("style_batches", `batch=eq.${B.batch}`, { status: "running", started_at: new Date().toISOString() });
await log(B.batch, "start", `Batch ${B.batch} (${B.label}). Balance ${balance}, cap ${B.credit_cap}, spent so far all batches ${totalSpent}`);

const canSpend = (c: number) => batchSpent + c <= B.credit_cap && totalSpent + (batchSpent - B.credits_spent) + c <= TOTAL_CAP;
const creators = await db(`style_creators?select=*&batch=eq.${B.batch}&status=neq.done&order=id.asc`);
const done: string[] = [], missing: string[] = [];

for (const c of creators) {
  try {
    const n = c.long_form ? 2 : PER, cost = c.long_form ? COST.long : COST.short;
    const urls = await findUrls(c.name, c.category, n, c.long_form);
    if (!urls.length) { await patch("style_creators", `id=eq.${c.id}`, { status: "not_found" }); missing.push(c.name); await log(B.batch, "warn", `${c.name}: no valid URLs found`); continue; }
    const jobs: { url: string; job: string }[] = [];
    for (const url of urls) {
      if (!canSpend(cost)) { await log(B.batch, "cap", `Batch cap reached before ${c.name} ${url}`); break; }
      const existing = await db(`style_videos?select=id,status&url=eq.${encodeURIComponent(url)}`);
      if (existing.length && existing[0].status === "done") continue;
      const res = c.long_form ? await tool("vidiq_video_watch", { video: url, prompt: EXTRACT }) : await tool("vidiq_watch_shortform_content", { url, prompt: EXTRACT });
      const job = pick(res.data, ["mcpJobId"], res.text);
      if (!job) { await log(B.batch, "warn", `${c.name}: no job id for ${url}: ${res.text.slice(0, 150)}`); continue; }
      batchSpent += cost;
      if (existing.length) await patch("style_videos", `id=eq.${existing[0].id}`, { job_id: job, status: "running", credits: cost });
      else await insert("style_videos", { creator_id: c.id, url, job_id: job, status: "running", credits: cost });
      await log(B.batch, "spend", `${c.name}: watch ${url}`, cost);
      jobs.push({ url, job });
    }
    await patch("style_batches", `batch=eq.${B.batch}`, { credits_spent: batchSpent });
    const analyses: string[] = [];
    for (const j of jobs) {
      let finished = false;
      for (let i = 0; i < 48 && !finished; i++) {
        await Bun.sleep(15000);
        const p = await tool("vidiq_job_poll", { mcpJobId: j.job });
        const status = String(pick(p.data, ["status"], p.text) || "");
        if (status === "completed") {
          const r = p.data?.result; const text = (typeof r === "string" ? r : r?.analysisText || r?.markdown || r?.text) || p.text;
          await patch("style_videos", `job_id=eq.${j.job}`, { status: "done", analysis: text }); analyses.push(`SOURCE ${j.url}\n${text}`); finished = true;
        } else if (["failed", "expired", "refunded"].includes(status)) {
          const refunded = p.data?.refunded ?? status === "refunded";
          if (refunded) { batchSpent -= c.long_form ? COST.long : COST.short; await patch("style_batches", `batch=eq.${B.batch}`, { credits_spent: batchSpent }); }
          await patch("style_videos", `job_id=eq.${j.job}`, { status: `failed${refunded ? "_refunded" : ""}` }); await log(B.batch, "warn", `${c.name}: job ${status} ${j.url}`); finished = true;
        }
      }
      if (!finished) await log(B.batch, "warn", `${c.name}: job still running after 12 min ${j.job} (left in DB as running)`);
    }
    if (!analyses.length) { missing.push(c.name); continue; }
    const card = await llm(`You are building a creator Style DNA card for a video production system. Creator: ${c.name} (${c.category}, ${c.country}). Below are scene-by-scene breakdowns of ${analyses.length} of their videos.\n\nWrite markdown with: 1) a 2-line summary; 2) a "Consensus DNA" table with rows Vibe, Tone, Energy (1-5), Pacing & edit, Camera & framing, Lighting & grade, Voice & delivery, Target age, Target audience, Hook pattern, Signature move — only what is consistent across videos; 3) "Variations" (what changes video to video); 4) "Higgsfield translation" — prompt fragments for camera, lighting, grade, pacing, plus an edit recipe (captions, SFX, zooms, transitions); 5) Sources. Then on the last line output a JSON object of the Consensus DNA fields prefixed with DNA_JSON: \n\n${analyses.join("\n\n---\n\n").slice(0, 60000)}`);
    const jm = card.match(/DNA_JSON:\s*(\{[\s\S]*\})\s*$/); let dna: any = null; try { dna = jm ? JSON.parse(jm[1]) : null; } catch {}
    const cardMd = card.replace(/DNA_JSON:[\s\S]*$/, "").trim();
    const ex = await db(`style_cards?select=creator_id&creator_id=eq.${c.id}`);
    if (ex.length) await patch("style_cards", `creator_id=eq.${c.id}`, { card_md: cardMd, dna, updated_at: new Date().toISOString() });
    else await insert("style_cards", { creator_id: c.id, card_md: cardMd, dna });
    await patch("style_creators", `id=eq.${c.id}`, { status: "done" }); done.push(c.name);
    await log(B.batch, "card", `${c.name}: card written from ${analyses.length} videos`);
  } catch (e: any) { missing.push(c.name); await log(B.batch, "error", `${c.name}: ${e.message}`); }
}

const remaining = await db(`style_creators?select=id&batch=eq.${B.batch}&status=eq.pending`);
await patch("style_batches", `batch=eq.${B.batch}`, { status: remaining.length ? "partial" : "done", finished_at: new Date().toISOString(), credits_spent: batchSpent });
const msg = `Style runner batch ${B.batch} (${B.label}): ${done.length} cards done${missing.length ? `, issues: ${missing.join(", ")}` : ""}. Credits this batch ${batchSpent}/${B.credit_cap}.${B.batch === 1 ? " Review the 3 pilot cards, then approve to unlock batches 2-6." : ""}`;
await log(B.batch, "done", msg); await notify(msg);
process.exit(0);

// TITAN code-motion renderer: an HTML template whose every pixel is a function of time t -> deterministic video frames -> ffmpeg.
// usage: node render.mjs <template.html> <out.mp4> [--data data.json] [--w 1080] [--h 1920] [--fps 30] [--dur S]
// Templates expose window.seek(t) and window.DURATION; they receive window.DATA (the JSON) and design on a 1080-wide stage (zoomed to --w).
// Needs Node 18+, `npm i playwright` (or a global install) and `npx playwright install chromium` once (Run-Editor.ps1 -Motion does it).
import { createRequire } from 'module'; import { spawn } from 'child_process'; import path from 'path'; import fs from 'fs'; import url from 'url';
const here = path.dirname(url.fileURLToPath(import.meta.url));
function load() {
  for (const base of [here + '/', process.cwd() + '/', ...(process.env.NODE_PATH || '').split(path.delimiter).filter(Boolean).map(p => p + '/'), '/opt/node22/lib/node_modules/']) {
    try { return createRequire(base)('playwright'); } catch (e) { /* next */ }
  }
  throw new Error('playwright not found: run `npm i playwright` in tools/motion, then `npx playwright install chromium`');
}
const args = process.argv.slice(2); const opt = (k, d) => { const i = args.indexOf('--' + k); return i >= 0 ? args[i + 1] : d; };
const [src, out] = args; const W = +opt('w', 1080), H = +opt('h', 1920), fps = +opt('fps', 30);
const data = opt('data') ? JSON.parse(fs.readFileSync(opt('data'), 'utf8')) : {};
const { chromium } = load();
const exe = process.env.PW_CHROMIUM;
const b = await chromium.launch(exe ? { executablePath: exe } : {});
const p = await b.newPage({ viewport: { width: W, height: H } });
await p.addInitScript(([d, w, h]) => { window.DATA = d; window.OUT_W = w; window.OUT_H = h; }, [data, W, H]);
await p.goto(url.pathToFileURL(path.resolve(src)).href);
await p.evaluate(() => document.fonts.ready);
const dur = +(opt('dur', 0)) || await p.evaluate(() => window.DURATION);
const n = Math.max(1, Math.round(dur * fps));
const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-i', '-', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', out], { stdio: ['pipe', 'inherit', 'inherit'] });
for (let i = 0; i < n; i++) {
  await p.evaluate(t => window.seek(t), i / fps);
  const buf = await p.screenshot({ type: 'jpeg', quality: 92 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
}
ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close();
console.log(JSON.stringify({ frames: n, dur, out }));

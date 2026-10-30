h=open("index.html").read()
h=h.replace("storyboard v4 · one room, one scene · 30 Oct 2026","storyboard v5 · your flow notes applied · 30 Oct 2026")
h=h.replace("Part 1 v4: one room, one outfit, one scene, so it plays like a film","Part 1 v5: your notes applied, texts as WhatsApp, no video call")
a=h.index('<p class="lede">');b=h.index("</p>",a)+4
h=h[:a]+"""<p class="lede">Your flow notes are in: she <b>declines the call and texts back instantly</b>, Trâm briefs her by <b>WhatsApp text</b>, the swipe men have <b>photos and ick-worthy bios</b>, and the torso montage is gone. To keep the one-film look, <b>texts now appear as bubbles over the characters own shots</b> (Hân typing, Trâm typing) instead of cutting to flat phone screens. Same room, same outfits.</p>"""+h[b:]
a=h.index('<div class="lanes">');b=h.index("</section>",a)
h=h[:a]+"""<div class="lanes">
      <div class="lane a"><b>Hân's bedroom, 11:04 pm · dating (pink)</b><span>Swipes through ick-worthy men (passport bros) → J's blurry body-only photos → match → "he types fast. a man of ac—"</span></div>
      <div class="lane x"><b>Interruption</b><span>An incoming video call from an unknown number. She declines and texts the number back instantly.</span></div>
      <div class="lane b"><b>Work · WhatsApp (green)</b><span>Trâm's texts, shown over Trâm typing in her own room: brief → booking approved → 2 rules → mask flies → "this is so sus" → "Perfect. Remember, only talk to me."</span></div>
      <div class="lane a"><b>Back to dating (pink)</b><span>J: "I'll reveal everything tomorrow, including my face" → "…have I ever seen his face?" → Day 1.</span></div>
    </div>
  """+h[b:]
a=h.index("const PANELS=[");b=h.index("];",a)+2
P=open("panels_v5.js").read()
h=h[:a]+P+h[b:]
h=h.replace("TÂM-1 (brief, 4 s, lip-sync to reference audio)\nLocked-off video-call camera, 28mm, 2% slow push-in. Trâm looks into the lens and speaks the exact line from the audio\nreference, lips in sync. Beat 1 (0-1.5 s): breezy smile, light head tilt on \"Hi!\". Beat 2 (1.5-3 s): small hand\ngesture as she says \"from afar\". Beat 3 (3-4 s): lowers her voice and eyes slightly on \"don't let him notice\".\nThe room, lamp, window and her grey tee do NOT change. No camera shake. Same 3D animated style, same face.",
"TRÂM-TYPING (4 s, no audio; WhatsApp bubbles are added in the edit)\nLocked-off propped-phone camera, 50mm waist-up, 2% slow push-in. Trâm looks down at her phone and types with both\nthumbs. Beat 1 (0-1.5 s): breezy half-smile, quick thumb taps. Beat 2 (1.5-3 s): she glances up toward the window\nfor a beat, then back at the phone. Beat 3 (3-4 s): a tiny satisfied nod as she sends. Her face stays in the upper\nhalf of the frame (bubbles sit below). The room, lamp, window and her grey tee do NOT change. Same face.")
h=h.replace("HÂN-ANSWER (1.8 s, no audio)\nMedium shot from the window side, 35mm, slow 2% push-in. Hân looks down at the phone propped on her knees, lets out a\ntiny sigh, pushes her mask up higher on her forehead with one finger, then puts on a bright polite smile as the call\nconnects. Warm lamp stays at the left of frame. The room does NOT change.",
"HÂN-TEXTS-BACK (2 s, no audio)\nWaist-up, 50mm, slow 2% push-in. Hân's thumb jabs DECLINE (off-screen), she sighs, then types very fast with both\nthumbs, her face sliding into a bright over-polite smile. Mask stays pushed up on her forehead. Warm lamp stays at the\nleft of frame. The room does NOT change.")
h=h.replace("<b>One look test first:</b> animate only <b>Trâm-1</b> and <b>Hân-answer</b> (about 24 credits)","<b>One look test first:</b> animate only <b>Trâm-typing</b> and <b>Hân-texts-back</b> (about 24 credits)")
h=h.replace("The work thread is now a <b>video call</b>, so Hân and Trâm talk face to face instead of cutting to text mock-ups. Nothing is animated yet.","Nothing is animated yet.")
h=h.replace('d.id.startsWith("v4-")','d.id.startsWith("v5-")').replace('board:"v4"','board:"v5"')
open("index.html","w").write(h)
print("built")

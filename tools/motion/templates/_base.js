// helpers: stage sizing, easing, clamp, theme from DATA
window.D = Object.assign({}, window.DATA || {});
const ease = { out: x => 1 - Math.pow(1 - x, 3), inout: x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2, back: x => 1 + 2.7 * Math.pow(x - 1, 3) + 1.7 * Math.pow(x - 1, 2) };
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const seg = (t, a, d) => clamp((t - a) / d);            // 0..1 progress of a segment starting at a, lasting d
function stage() {
  const s = document.getElementById('stage'); const z = (window.OUT_W || 1080) / 1080;
  s.style.height = (1080 * (window.OUT_H || 1920) / (window.OUT_W || 1080)) + 'px'; s.style.transform = `scale(${z})`;
  const th = D.theme || {}; for (const [k, v] of Object.entries(th)) document.documentElement.style.setProperty('--' + k, v);
  return s;
}

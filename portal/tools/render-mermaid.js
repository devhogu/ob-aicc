// Draw Mermaid diagrams to SVG in one headless-browser session, with the portal font loaded before the text is measured.
// Input (stdin): {"jobs":[{"key","code"}], "font":"path to woff2", "mermaid":"path to mermaid.min.js", "puppeteer":"path", "chrome":"path"}
// Output (stdout): {"<key>":{"light":"<svg>","dark":"<svg>"}} ; a diagram that fails is absent.
const fs = require('fs');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
const puppeteer = require(input.puppeteer);

const FONT = "'Golos Text', 'DejaVu Sans', Arial, sans-serif";
const THEMES = {
  light: {
    vars: { primaryColor: '#F3EEFB', primaryTextColor: '#1E1A26', primaryBorderColor: '#7A56C2', lineColor: '#4A4553', secondaryColor: '#E8F0FF', tertiaryColor: '#FFFFFF', noteBkgColor: '#FFF4DA', noteTextColor: '#1E1A26', edgeLabelBackground: '#FFFFFF', clusterBkg: '#F8F6FB', clusterBorder: '#BDB2D6', titleColor: '#1E1A26', actorBkg: '#F3EEFB', actorBorder: '#7A56C2', actorTextColor: '#1E1A26', signalColor: '#4A4553', signalTextColor: '#1E1A26', labelBoxBkgColor: '#F3EEFB', labelBoxBorderColor: '#7A56C2', labelTextColor: '#1E1A26', loopTextColor: '#1E1A26', activationBkgColor: '#E8F0FF', sequenceNumberColor: '#FFFFFF' },
    css: { node: '#F3EEFB', nodeStroke: '#7A56C2', gate: '#FCE8F2', gateStroke: '#C50068', iface: '#E4EEFF', ifaceStroke: '#185ABC', ext: '#E9F6EC', extStroke: '#2E7D4F', edgeBg: '#FFFFFF', text: '#1E1A26' }
  },
  dark: {
    vars: { primaryColor: '#2B2433', primaryTextColor: '#F2EEF6', primaryBorderColor: '#B79CE8', lineColor: '#C7BED3', secondaryColor: '#1F2E47', tertiaryColor: '#18181B', noteBkgColor: '#3D2B13', noteTextColor: '#F2EEF6', edgeLabelBackground: '#18181B', clusterBkg: '#211D27', clusterBorder: '#5A4F6B', titleColor: '#F2EEF6', actorBkg: '#2B2433', actorBorder: '#B79CE8', actorTextColor: '#F2EEF6', signalColor: '#C7BED3', signalTextColor: '#F2EEF6', labelBoxBkgColor: '#2B2433', labelBoxBorderColor: '#B79CE8', labelTextColor: '#F2EEF6', loopTextColor: '#F2EEF6', activationBkgColor: '#1F2E47', sequenceNumberColor: '#18181B' },
    css: { node: '#2B2433', nodeStroke: '#B79CE8', gate: '#4A2238', gateStroke: '#FF85C1', iface: '#1F2E47', ifaceStroke: '#8AB4FF', ext: '#1D3326', extStroke: '#86D9A0', edgeBg: '#18181B', text: '#F2EEF6' }
  }
};

function themeCSS(c) {
  return [
    '.node rect,.node polygon,.node path,.node circle,.node ellipse{stroke-width:1.5px;filter:drop-shadow(0 1px 2px rgba(0,0,0,.22));}',
    '.node rect{rx:12px;ry:12px;}',
    '.node.gate rect,.node.gate polygon,.node.gate path{fill:' + c.gate + ' !important;stroke:' + c.gateStroke + ' !important;}',
    '.node.iface rect,.node.iface polygon,.node.iface path{fill:' + c.iface + ' !important;stroke:' + c.ifaceStroke + ' !important;}',
    '.node.ext rect,.node.ext polygon,.node.ext path{fill:' + c.ext + ' !important;stroke:' + c.extStroke + ' !important;}',
    '.cluster rect{rx:16px;ry:16px;stroke-width:1.2px;}',
    '.edgeLabel,.edgeLabel p,.labelBkg{background-color:' + c.edgeBg + ' !important;color:' + c.text + ' !important;}',
    '.edgeLabel p{margin:0;padding:1px 5px;border-radius:6px;}',
    'foreignObject{overflow:visible;}',
    '.nodeLabel p,.nodeLabel{margin:0;line-height:1.3;}',
    '.flowchart-link,.messageLine0,.messageLine1{stroke-width:1.5px;}'
  ].join('');
}

(async () => {
  const browser = await puppeteer.launch({ executablePath: input.chrome, args: ['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage'], headless: 'shell' });
  const page = await browser.newPage();
  const b64 = fs.readFileSync(input.font).toString('base64');
  await page.setContent('<!doctype html><html><head><style>@font-face{font-family:"Golos Text";font-weight:100 900;src:url(data:font/woff2;base64,' + b64 + ') format("woff2");}body{font-family:"Golos Text",sans-serif;}</style></head><body><div id="c">Golos</div></body></html>');
  await page.addScriptTag({ path: input.mermaid });
  await page.evaluate(async () => { await document.fonts.load('15px "Golos Text"'); await document.fonts.load('600 15px "Golos Text"'); await document.fonts.ready; });
  const out = {};
  for (const theme of ['light', 'dark']) {
    const t = THEMES[theme];
    await page.evaluate((cfg) => mermaid.initialize(cfg), {
      startOnLoad: false, securityLevel: 'strict', theme: 'base', fontFamily: FONT, themeCSS: themeCSS(t.css),
      themeVariables: Object.assign({ fontFamily: FONT, fontSize: '14px' }, t.vars),
      flowchart: { htmlLabels: true, useMaxWidth: true, padding: 10, nodeSpacing: 30, rankSpacing: 44, curve: 'basis', wrappingWidth: 260 },
      sequence: { useMaxWidth: true, wrap: true, width: 170, mirrorActors: false }
    });
    for (const job of input.jobs) {
      try {
        const svg = await page.evaluate(async (id, code) => { const r = await mermaid.render(id, code); return r.svg; }, 'mm-' + job.key + '-' + theme, job.code);
        (out[job.key] = out[job.key] || {})[theme] = svg;
      } catch (e) {
        process.stderr.write('diagram ' + job.key + ' (' + theme + '): ' + String(e.message || e).slice(0, 160) + '\n');
      }
    }
  }
  await browser.close();
  process.stdout.write(JSON.stringify(out));
})().catch((e) => { process.stderr.write(String(e && e.stack || e) + '\n'); process.exit(1); });

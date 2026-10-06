// START_MODULE_CONTRACT
//   PURPOSE: Read project diagrams at useful scale with native, accessible controls.
//   SCOPE: Progressive dialog expansion, pan, zoom, fit, close and focus return.
//   DEPENDS: M-PORTAL-NEIGHBOURS
//   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
//   MAP_MODE: SUMMARY
// END_MODULE_CONTRACT
// START_MODULE_MAP
//   open - move the selected SVG into a native modal without duplicate IDs
//   scale - apply bounded scaling and preserve the viewport center
//   restore - return the original diagram and keyboard focus on close
// END_MODULE_MAP
(() => {
  const script = document.currentScript;
  const ui = JSON.parse(script.dataset.projectUi);
  const triggers = [...document.querySelectorAll('.project-diagram-open')];
  document.body.classList.add('project-enhanced');
  if (!triggers.length) return;
  let diagram, origin, trigger, width, height, zoom = 1;
  const dialog = document.createElement('dialog');
  dialog.className = 'project-viewer';
  dialog.id = 'project-diagram-viewer';
  dialog.setAttribute('aria-labelledby', 'project-diagram-title');
  const shell = document.createElement('div'); shell.className = 'project-viewer-shell';
  const bar = document.createElement('div'); bar.className = 'project-viewer-bar';
  const title = document.createElement('h2'); title.className = 'project-viewer-title'; title.id = 'project-diagram-title';
  const controls = document.createElement('div'); controls.className = 'project-viewer-controls';
  const viewport = document.createElement('div'); viewport.className = 'project-viewer-viewport';
  viewport.tabIndex = 0; viewport.setAttribute('role', 'region'); viewport.setAttribute('aria-label', ui.view);
  const stage = document.createElement('div'); stage.className = 'project-viewer-stage'; viewport.append(stage);
  const hint = document.createElement('p'); hint.className = 'project-viewer-hint'; hint.textContent = ui.hint;
  const output = document.createElement('output'); output.setAttribute('aria-live', 'polite');
  function button(label, action, id) {
    const b = document.createElement('button'); b.type = 'button'; b.className = 'oc-button';
    b.textContent = label; b.dataset.projectAction = id; b.addEventListener('click', action); controls.append(b); return b;
  }
  const smaller = button('−', () => scale(zoom - .25, true), 'out'); smaller.setAttribute('aria-label', ui.out);
  controls.append(output);
  const larger = button('+', () => scale(zoom + .25, true), 'in'); larger.setAttribute('aria-label', ui.in);
  button(ui.fit, () => fit(), 'fit'); button(ui.actual, () => scale(1, true), 'actual');
  button(ui.close, () => dialog.close(), 'close');
  bar.append(title, controls); shell.append(bar, viewport, hint); dialog.append(shell); document.body.append(dialog);
  function scale(value, preserve) {
    const x = (viewport.scrollLeft + viewport.clientWidth / 2) / (width * zoom + 48);
    const y = (viewport.scrollTop + viewport.clientHeight / 2) / (height * zoom + 48);
    zoom = Math.max(.01, Math.min(4, value));
    diagram.style.setProperty('width', width * zoom + 'px', 'important');
    diagram.style.setProperty('height', height * zoom + 'px', 'important');
    stage.style.width = width * zoom + 'px'; stage.style.height = height * zoom + 'px';
    output.value = Math.round(zoom * 100) + '%'; smaller.disabled = zoom <= .01; larger.disabled = zoom >= 4;
    if (preserve) { viewport.scrollLeft = x * (width * zoom + 48) - viewport.clientWidth / 2; viewport.scrollTop = y * (height * zoom + 48) - viewport.clientHeight / 2; }
  }
  function fit() {
    scale(Math.min((viewport.clientWidth - 48) / width, (viewport.clientHeight - 48) / height), false);
    viewport.scrollLeft = 0; viewport.scrollTop = 0;
  }
  function restore() {
    if (!diagram) return;
    diagram.style.removeProperty('width'); diagram.style.removeProperty('height');
    origin.replaceWith(diagram); trigger.setAttribute('aria-expanded', 'false'); trigger.focus();
    diagram = null; document.body.style.overflow = '';
  }
  function open(b) {
    trigger = b; diagram = b.closest('figure').querySelector('svg');
    const box = diagram.viewBox.baseVal; width = box.width; height = box.height;
    if (!(width > 0 && height > 0)) { diagram = null; return; }
    title.textContent = diagram.getAttribute('aria-label') || ui.view;
    origin = document.createComment('project diagram origin'); diagram.replaceWith(origin); stage.append(diagram);
    trigger.setAttribute('aria-expanded', 'true'); dialog.showModal(); document.body.style.overflow = 'hidden';
    fit(); viewport.focus();
  }
  triggers.forEach(b => { b.setAttribute('aria-controls', dialog.id); b.setAttribute('aria-expanded', 'false'); b.addEventListener('click', () => open(b)); });
  dialog.addEventListener('close', restore);
  dialog.addEventListener('click', e => { if (e.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', e => {
    if (e.key === '+' || e.key === '=') { e.preventDefault(); scale(zoom + .25, true); }
    if (e.key === '-') { e.preventDefault(); scale(zoom - .25, true); }
  });
  viewport.addEventListener('wheel', e => {
    if (!e.ctrlKey && !e.metaKey) return;
    e.preventDefault(); scale(zoom + (e.deltaY < 0 ? .15 : -.15), true);
  }, {passive: false});
})();

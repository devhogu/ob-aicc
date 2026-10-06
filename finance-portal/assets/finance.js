/* Open linked stage details and keep keyboard focus inside their retained modal. */
(() => {
  const tabs = [...document.querySelectorAll('.problems-tab-input')];
  function syncTabs() {
    for (const input of tabs) {
      const label = document.querySelector(`label[for="${CSS.escape(input.id)}"]`);
      if (label) label.setAttribute('aria-selected', String(input.checked));
    }
  }
  for (const input of tabs) {
    const label = document.querySelector(`label[for="${CSS.escape(input.id)}"]`);
    if (!label) continue;
    input.addEventListener('focus', () => label.classList.add('finance-tab-focus'));
    input.addEventListener('blur', () => label.classList.remove('finance-tab-focus'));
    input.addEventListener('change', syncTabs);
  }
  syncTabs();

  const modal = document.getElementById('stageModal');
  if (!modal) return;
  const close = modal.querySelector('.modal__close');
  let trigger = null;

  function restoreFocus() {
    if (!trigger || modal.classList.contains('is-open')) return;
    trigger.focus({ preventScroll: true });
    trigger = null;
  }

  document.addEventListener('click', event => {
    const stage = event.target.closest('.flow-stages__stage');
    if (!stage || !modal.classList.contains('is-open')) return;
    trigger = stage;
    const title = modal.querySelector('.modal__title');
    if (title) {
      title.id = 'stage-modal-title';
      modal.setAttribute('aria-labelledby', title.id);
    }
    close.focus({ preventScroll: true });
  });

  modal.addEventListener('click', event => {
    if (event.target === modal || event.target.closest('.modal__close')) restoreFocus();
  });

  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') restoreFocus();
    if (event.key === 'Tab' && modal.classList.contains('is-open')) {
      event.preventDefault();
      close.focus({ preventScroll: true });
    }
  });

  function openLinkedStage() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (e) { return; }
    const stage = document.getElementById(id);
    if (!stage || !stage.matches('.flow-stages__stage')) return;
    for (let parent = stage.parentElement; parent; parent = parent.parentElement) {
      if (parent.tagName === 'DETAILS') parent.open = true;
    }
    stage.scrollIntoView({ block: 'center' });
    stage.click();
  }
  // Initial fragment navigation focuses its target before load. Open afterward
  // so that the dialog keeps focus instead of the stage button behind it.
  if (document.readyState === 'complete') openLinkedStage();
  else window.addEventListener('load', openLinkedStage, { once: true });
  window.addEventListener('hashchange', openLinkedStage);
})();

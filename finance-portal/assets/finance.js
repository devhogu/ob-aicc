/* Keep keyboard focus inside the retained stage modal and return it on close. */
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
})();

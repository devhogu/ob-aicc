/* One read-only selection mechanism. Registry records remain workflow authority. */
(() => {
  document.querySelectorAll('[data-kanban-workspace]').forEach(root => {
    let opener, panel;
    function clear(returnFocus = false) {
      if (panel) { panel.hidden = true; panel.querySelector('.kb-detail-body').replaceChildren(); }
      root.querySelectorAll('[data-kb-open]').forEach(card => {card.removeAttribute('aria-current');card.setAttribute('aria-expanded','false');});
      if (returnFocus && opener && !opener.closest('[hidden]')) opener.focus();
      opener = panel = undefined;
    }
    root.querySelectorAll('[data-kb-open]').forEach(card => {
      const view = card.closest('[data-pf-panel], [data-dl-panel]');
      const shell = view?.querySelector('[data-kb-panel]');
      const template = [...root.querySelectorAll('template[data-kb-detail]')].find(t => t.dataset.kbDetail === card.dataset.kbOpen);
      if (!shell || !template) return;
      shell.id ||= 'kb-detail-'+view.id;
      card.setAttribute('aria-controls',shell.id);card.setAttribute('aria-expanded','false');
      card.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey || event.button !== 0) return;
        event.preventDefault();clear();opener = card;panel = shell;
        panel.querySelector('.kb-detail-body').replaceChildren(template.content.cloneNode(true));
        panel.querySelector('[data-kb-full]').href = card.href;
        panel.querySelector('[data-kb-identity]').textContent = card.dataset.kbOpen;
        const heading = panel.querySelector('.kb-detail-body h2');
        heading.id = panel.id+'-heading';heading.tabIndex = -1;
        panel.setAttribute('aria-labelledby',heading.id);panel.hidden = false;
        card.setAttribute('aria-current','true');card.setAttribute('aria-expanded','true');
        if (event.detail === 0) heading.focus();
      });
    });
    root.querySelectorAll('[data-kb-close]').forEach(button => button.addEventListener('click', () => clear(true)));
    root.addEventListener('keydown', event => {if (event.key === 'Escape' && panel) {event.preventDefault();clear(true);}});
    root.addEventListener('kanban:refresh', () => {if (opener?.closest('[hidden]')) clear();});
  });
})();

/* Progressive reading controls. Decisions and workflow state stay in the Registry. */
(() => {
  const root = document.querySelector('.pf-content');
  if (!root) return;
  const tabs = [...root.querySelectorAll('[data-pf-tab]')];
  const panels = [...root.querySelectorAll('[data-pf-panel]')];
  function show(key, focus = false) {
    if (!panels.some(p => p.id === key)) key = 'board';
    panels.forEach(p => { p.hidden = p.id !== key; });
    tabs.forEach(t => { t.setAttribute('aria-selected', String(t.dataset.pfTab === key)); t.tabIndex = t.dataset.pfTab === key ? 0 : -1; });
    if (focus) tabs.find(t => t.dataset.pfTab === key)?.focus();
    root.dispatchEvent(new Event('kanban:refresh'));
    const filter = root.querySelector('.pf-filter');
    if (filter) filter.hidden = !['board', 'review'].includes(key);
  }
  if (tabs.length) {
    root.classList.add('pf-enhanced');
    root.querySelector('.pf-tabs').setAttribute('role','tablist');
    panels.forEach(p => {p.setAttribute('role','tabpanel');p.setAttribute('aria-labelledby','pf-tab-'+p.id);});
    tabs.forEach((tab, index) => {
      tab.id = 'pf-tab-'+tab.dataset.pfTab;tab.setAttribute('role','tab');tab.setAttribute('aria-controls',tab.dataset.pfTab);
      tab.addEventListener('click', event => {event.preventDefault();history.replaceState(null,'','#'+tab.dataset.pfTab);show(tab.dataset.pfTab);});
      tab.addEventListener('keydown', event => {
        let next;
        if (event.key === 'ArrowRight') next = (index+1)%tabs.length;
        if (event.key === 'ArrowLeft') next = (index+tabs.length-1)%tabs.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = tabs.length-1;
        if (next !== undefined) {event.preventDefault();tabs[next].click();tabs[next].focus();}
      });
    });
    show(location.hash.slice(1));
    addEventListener('hashchange',()=>show(location.hash.slice(1)));
  } else {
    const filter = root.querySelector('.pf-filter');if(filter) filter.hidden = false;
  }
  const search = root.querySelector('[data-pf-search]');
  const priority = root.querySelector('[data-pf-priority]');
  function filter() {
    const q = (search?.value || '').trim().toLocaleLowerCase();const selected = priority?.value || '';
    const visible = new Set();
    root.querySelectorAll('[data-pf-item]').forEach(card => {
      card.hidden = !(card.dataset.find.includes(q) && (!selected || card.dataset.priority.split(' ').includes(selected)));
      if(!card.hidden && card.dataset.kind === 'ordinary') visible.add(card.dataset.pfItem);
    });
    const output = root.querySelector('[data-pf-visible]');
    if (output) {output.dataset.label ||= output.textContent.split(':')[0];output.textContent = output.dataset.label+': '+visible.size;}
    root.querySelectorAll('[data-pf-column]').forEach(col => {
      col.querySelector('.pf-empty').hidden = !!col.querySelector('[data-pf-item]:not([hidden])');
    });
    const empty = root.querySelector('.pf-review-empty');
    if(empty) empty.hidden = !!root.querySelector('#review [data-pf-item]:not([hidden])');
    root.dispatchEvent(new Event('kanban:refresh'));
  }
  search?.addEventListener('input',filter);priority?.addEventListener('change',filter);
})();

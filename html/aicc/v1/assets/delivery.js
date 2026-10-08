/* Progressive reading controls. Decisions and workflow state stay in the Registry. */
(() => {
  const root = document.querySelector('.dl-content');
  if (!root) return;
  const tabs = [...root.querySelectorAll('[data-dl-tab]')];
  const panels = [...root.querySelectorAll('[data-dl-panel]')];
  function show(key, focus = false) {
    if (!panels.some(p => p.id === key)) key = 'board';
    panels.forEach(p => { p.hidden = p.id !== key; });
    tabs.forEach(t => { t.setAttribute('aria-selected', String(t.dataset.dlTab === key)); t.tabIndex = t.dataset.dlTab === key ? 0 : -1; });
    if (focus) tabs.find(t => t.dataset.dlTab === key)?.focus();
    root.dispatchEvent(new Event('kanban:refresh'));
    const filter = root.querySelector('.dl-filters');
    if (filter) filter.hidden = !['intake'].includes(key);
  }
  if (tabs.length) {
    root.classList.add('dl-enhanced');
    root.querySelector('.dl-tabs').setAttribute('role','tablist');
    panels.forEach(p => {p.setAttribute('role','tabpanel');p.setAttribute('aria-labelledby','dl-tab-'+p.id);});
    tabs.forEach((tab, index) => {
      tab.id = 'dl-tab-'+tab.dataset.dlTab;tab.setAttribute('role','tab');tab.setAttribute('aria-controls',tab.dataset.dlTab);
      tab.addEventListener('click', event => {event.preventDefault();history.replaceState(null,'','#'+tab.dataset.dlTab);show(tab.dataset.dlTab);});
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
    const filter = root.querySelector('.dl-filters');if(filter) filter.hidden = false;
  }
  const search = root.querySelector('[data-dl-search]');
  const priority = root.querySelector('[data-dl-priority]');
  function filter() {
    const q = (search?.value || '').trim().toLocaleLowerCase();const selected = priority?.value || '';
    const visible = new Set();
    root.querySelectorAll('[data-dl-item]').forEach(card => {
      card.hidden = !(card.dataset.find.includes(q) && (!selected || card.dataset.priority.split(' ').includes(selected)));
      if(!card.hidden) visible.add(card.dataset.dlItem);
    });
    root.dispatchEvent(new Event('kanban:refresh'));
    const output = root.querySelector('[data-dl-count]');
    if (output) {output.dataset.label ||= output.textContent.split(':')[0];output.textContent = output.dataset.label+': '+visible.size;}
  }
  search?.addEventListener('input',filter);priority?.addEventListener('change',filter);
})();

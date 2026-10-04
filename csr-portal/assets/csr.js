(() => {
  const root = document.documentElement;
  const body = document.body;
  const lang = body.dataset.language;
  const words = lang === 'ru'
    ? {light: 'Светлая тема', dark: 'Темная тема', focus: 'Развернуть схему', restore: 'Показать навигацию'}
    : {light: 'Light theme', dark: 'Dark theme', focus: 'Expand map', restore: 'Show navigation'};
  const theme = document.getElementById('csr-theme');
  function labelTheme() {
    const next = root.dataset.theme === 'dark' ? words.light : words.dark;
    theme.textContent = next;
    theme.setAttribute('aria-label', next);
  }
  theme.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('obank-csr-theme', root.dataset.theme); } catch {}
    labelTheme();
  });
  labelTheme();

  const sections = [...document.querySelectorAll('[data-document]')];
  const navLinks = [...document.querySelectorAll('[data-doc-link]')];
  const header = document.querySelector('.csr-header');
  function showCurrentSection() {
    const threshold = header.getBoundingClientRect().bottom + 112;
    let current = sections[0];
    for (const section of sections) {
      if (section.getBoundingClientRect().top <= threshold) current = section;
      else break;
    }
    let chosen = null;
    navLinks.forEach(link => {
      const active = link.dataset.docLink === current.dataset.document;
      link.classList.toggle('active', active);
      if (active) chosen = link;
    });
    document.querySelectorAll('.nav-doc').forEach(item => item.classList.toggle('is-active', chosen?.closest('.nav-doc') === item));
    if (chosen) {
      const summary = chosen.closest('.nav-doc')?.querySelector('summary');
      document.getElementById('current-section').textContent = summary?.textContent.trim() || chosen.textContent.trim();
    }
  }
  let scrollPending = false;
  window.addEventListener('scroll', () => {
    if (scrollPending) return;
    scrollPending = true;
    requestAnimationFrame(() => { scrollPending = false; showCurrentSection(); });
  }, {passive: true});
  window.addEventListener('hashchange', showCurrentSection);
  showCurrentSection();

  const target = location.hash && document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (target) {
    const doc = target.closest('.doc-panel');
    const nav = doc && document.querySelector(`[data-doc-link="${doc.dataset.document}"]`);
    if (nav) {
      const detail = nav.closest('.nav-doc');
      const group = nav.closest('.nav-group');
      if (detail) detail.open = true;
      if (group) group.open = true;
    }
  }
  document.querySelectorAll('.table-wrap').forEach(table => {
    if (table.scrollWidth > table.clientWidth + 1) {
      table.tabIndex = 0;
      table.setAttribute('role', 'region');
      table.setAttribute('aria-label', table.dataset.csrTableLabel);
    }
  });

  const cards = [...document.querySelectorAll('[data-csr-step]')];
  function select(card, updateUrl = false) {
    cards.forEach(item => item.setAttribute('aria-pressed', String(item === card)));
    document.getElementById('csr-step-title').textContent = card.querySelector('strong').textContent;
    document.getElementById('csr-step-work').textContent = card.dataset.work;
    document.getElementById('csr-step-assist').textContent = card.dataset.assist;
    document.getElementById('csr-step-owner').textContent = card.dataset.owner;
    if (updateUrl) {
      const url = new URL(location.href);
      url.searchParams.set('step', card.dataset.csrStep);
      history.replaceState(null, '', url);
    }
  }
  cards.forEach(card => card.addEventListener('click', () => select(card, true)));
  const initial = new URLSearchParams(location.search).get('step');
  select(cards.find(card => card.dataset.csrStep === initial) || cards[0]);

  const focus = document.getElementById('csr-map-focus');
  focus.addEventListener('click', () => {
    const on = body.classList.toggle('csr-map-focused');
    focus.setAttribute('aria-pressed', String(on));
    focus.textContent = on ? words.restore : words.focus;
  });

  document.querySelectorAll('[data-csr-language]').forEach(link => link.addEventListener('click', event => {
    event.preventDefault();
    const url = new URL(link.href);
    const selected = cards.find(card => card.getAttribute('aria-pressed') === 'true');
    if (selected) url.searchParams.set('step', selected.dataset.csrStep);
    if (location.hash) {
      const hashMap = JSON.parse(document.getElementById('csr-hash-map').textContent);
      const sourceId = decodeURIComponent(location.hash.slice(1));
      url.hash = hashMap[sourceId] || (lang === 'ru' ? 'en-start' : 'ru-start');
    }
    location.href = url.href;
  }));
})();

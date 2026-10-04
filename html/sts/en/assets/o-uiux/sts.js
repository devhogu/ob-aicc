(() => {
  const root = document.documentElement;
  const button = document.getElementById('theme-switch');
  try { root.dataset.theme = localStorage.getItem('obank-sts-theme') === 'light' ? 'light' : 'dark'; }
  catch { root.dataset.theme = 'dark'; }
  function labelTheme() {
    const next = root.dataset.theme === 'dark' ? 'Light' : 'Dark';
    button.textContent = `${next} theme`;
    button.setAttribute('aria-label', `Switch to ${next.toLowerCase()} theme`);
  }
  button.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('obank-sts-theme', root.dataset.theme); } catch {}
    labelTheme();
  });
  labelTheme();

  const details = document.querySelector('.o-nav details');
  const narrow = matchMedia('(max-width: 1100px)');
  function adapt() { details.open = !narrow.matches; }
  narrow.addEventListener('change', adapt);
  adapt();
  details.querySelectorAll('nav a').forEach(link => link.addEventListener('click', () => {
    if (narrow.matches) details.open = false;
  }));

  const focus = document.getElementById('sts-map-focus');
  if (focus) {
    focus.addEventListener('click', () => {
      const on = document.body.classList.toggle('sts-map-focus');
      focus.setAttribute('aria-pressed', String(on));
      focus.textContent = on ? 'Show navigation' : 'Expand map';
    });
    const cards = [...document.querySelectorAll('[data-sts-state]')];
    function select(card) {
      cards.forEach(item => item.setAttribute('aria-pressed', String(item === card)));
      document.getElementById('sts-state-title').textContent = card.querySelector('strong').textContent;
      document.getElementById('sts-state-summary').textContent = card.querySelector('small').textContent;
      document.getElementById('sts-state-group').textContent = card.dataset.group;
      document.getElementById('sts-state-link').href = card.dataset.target;
    }
    cards.forEach(card => card.addEventListener('click', () => select(card)));
    if (cards.length) select(cards[0]);
  }

  // The source reference page has click tabs; add the keyboard model expected by their ARIA roles.
  const tabs = [...document.querySelectorAll('[data-flow-tab]')];
  tabs.forEach(tab => tab.addEventListener('keydown', event => {
    const keys = ['ArrowLeft', 'ArrowRight', 'Home', 'End'];
    if (!keys.includes(event.key)) return;
    event.preventDefault();
    const index = tabs.indexOf(tab);
    const next = event.key === 'Home' ? 0 : event.key === 'End' ? tabs.length - 1
      : (index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
    tabs[next].focus();
    tabs[next].click();
  }));
  tabs.forEach(tab => { tab.tabIndex = tab.getAttribute('aria-selected') === 'true' ? 0 : -1; });
  tabs.forEach(tab => tab.addEventListener('click', () => {
    tabs.forEach(item => { item.tabIndex = item === tab ? 0 : -1; });
  }));

  document.querySelectorAll('.visual-stage').forEach(stage => {
    if (stage.scrollWidth > stage.clientWidth + 1) {
      stage.setAttribute('role', 'region');
      stage.setAttribute('tabindex', '0');
      if (!stage.hasAttribute('aria-label')) stage.setAttribute('aria-label', 'Scrollable STS visual model');
    }
  });
  const selected = location.hash ? document.getElementById(location.hash.slice(1)) : null;
  if (selected instanceof Element && selected.matches('[data-state]')) selected.click();
})();

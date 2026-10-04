const details = document.querySelector('.o-nav details');
const narrow = matchMedia('(max-width: 1100px)');
function adaptNavigation() { details.open = !narrow.matches; }
narrow.addEventListener('change', adaptNavigation);
adaptNavigation();

const themeButton = document.getElementById('theme-switch');
function updateThemeLabel() {
  const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
  themeButton.textContent = `${next[0].toUpperCase()}${next.slice(1)} theme`;
  themeButton.setAttribute('aria-label', `Switch to ${next} theme`);
}
themeButton.addEventListener('click', () => {
  const root = document.documentElement;
  root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
  try { localStorage.setItem('obank-lab-theme', root.dataset.theme); } catch {}
  updateThemeLabel();
});
updateThemeLabel();

const links = [...document.querySelectorAll('.o-nav nav a')];
links.forEach(link => link.addEventListener('click', () => {
  links.forEach(item => item.removeAttribute('aria-current'));
  link.setAttribute('aria-current', 'location');
  if (narrow.matches) details.open = false;
}));

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    const current = entries.filter(entry => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (!current) return;
    const selected = links.find(link => link.hash === `#${current.target.id}`);
    if (!selected) return;
    links.forEach(item => item.removeAttribute('aria-current'));
    selected.setAttribute('aria-current', 'location');
  }, { rootMargin: '-12% 0px -55% 0px' });
  document.querySelectorAll('.lab-content > section[id]').forEach(section => observer.observe(section));
}

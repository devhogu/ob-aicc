(function () {
  var root = document.documentElement;

  var themeButton = document.querySelector('.site-theme-button');
  function syncTheme() {
    if (!themeButton) return;
    var dark = root.getAttribute('data-theme') === 'dark';
    themeButton.setAttribute('aria-label', dark ? themeButton.dataset.toLight : themeButton.dataset.toDark);
    themeButton.setAttribute('aria-pressed', dark ? 'true' : 'false');
  }
  if (themeButton) {
    themeButton.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem('aicc-theme', next); } catch (e) {}
      syncTheme();
    });
    syncTheme();
  }

  var menuButton = document.querySelector('.site-menu-button');
  var nav = document.getElementById('site-nav');
  if (menuButton && nav) {
    menuButton.addEventListener('click', function () {
      var open = menuButton.getAttribute('aria-expanded') !== 'true';
      menuButton.setAttribute('aria-expanded', open ? 'true' : 'false');
      menuButton.setAttribute('aria-label', open ? menuButton.dataset.close : menuButton.dataset.open);
      nav.classList.toggle('is-open', open);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        menuButton.click();
        menuButton.focus();
      }
    });
  }

  document.querySelectorAll('.site-lang a[data-lang]').forEach(function (a) {
    a.addEventListener('click', function () {
      try { localStorage.setItem('aicc-lang', a.dataset.lang); } catch (e) {}
    });
  });
})();

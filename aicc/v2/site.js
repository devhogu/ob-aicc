/* AI Competence Hub: theme, search and navigation. No external requests; the search index loads as a script so the site also opens from a folder. */
(function () {
  var script = document.currentScript;
  var d = script ? script.dataset : {};
  var root = document.documentElement;
  var themeBtn = document.getElementById('theme-switch');
  function label() {
    if (!themeBtn) return;
    var t = root.dataset.theme === 'dark' ? d.tLight : d.tDark;
    themeBtn.setAttribute('aria-label', t);
    themeBtn.title = t;
  }
  if (themeBtn) {
    label();
    themeBtn.addEventListener('click', function () {
      var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem('hub-theme', next); } catch (e) {}
      label();
    });
  }
  var navd = document.querySelector('.o-nav details');
  if (navd && window.matchMedia('(max-width: 1100px)').matches) navd.removeAttribute('open');

  var input = document.getElementById('q');
  var results = document.getElementById('results');
  var index = Array.isArray(window.AICC_SEARCH_INDEX) ? window.AICC_SEARCH_INDEX : [];
  function tokens(s) { return s.toLowerCase().split(/[^\p{L}\p{N}]+/u).filter(Boolean); }
  function run() {
    var q = tokens(input.value);
    if (!q.length) { results.hidden = true; return; }
    var scored = [];
    index.forEach(function (e) {
      var h = (e.h + ' ' + e.t).toLowerCase(), x = e.x.toLowerCase(), s = 0, ok = true;
      q.forEach(function (w) {
        var inH = h.indexOf(w) >= 0, inX = x.indexOf(w) >= 0;
        if (!inH && !inX) ok = false; else s += (inH ? 3 : 0) + (inX ? 1 : 0);
      });
      if (tokens(e.h).join(' ') === q.join(' ')) s += 4;
      if (ok) scored.push([s, e]);
    });
    scored.sort(function (a, b) { return b[0] - a[0]; });
    results.innerHTML = '';
    if (!scored.length) { var p = document.createElement('p'); p.textContent = d.tNone; results.appendChild(p); }
    scored.slice(0, 12).forEach(function (r) {
      var a = document.createElement('a'); a.href = (d.root === '.' ? '' : d.root + '/') + r[1].u;
      var b = document.createElement('strong'); b.textContent = r[1].h; a.appendChild(b);
      var s = document.createElement('small'); s.textContent = ' ' + r[1].t; a.appendChild(s);
      results.appendChild(a);
    });
    results.hidden = false;
  }
  if (input) {
    input.addEventListener('input', run);
    document.addEventListener('click', function (e) { if (!results.contains(e.target) && e.target !== input) results.hidden = true; });
    input.addEventListener('keydown', function (e) { if (e.key === 'Escape') results.hidden = true; });
  }
  function reveal() {
    var target;
    try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch (e) { return; }
    for (var node = target; node; node = node.parentElement) if (node.tagName === 'DETAILS') node.open = true;
  }
  reveal();
  window.addEventListener('hashchange', reveal);
})();

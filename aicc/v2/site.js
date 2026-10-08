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

  // tooltips that follow the pointer, and appear on keyboard focus
  var tip = document.createElement('div');
  tip.className = 'tip'; tip.id = 'tip'; tip.setAttribute('role', 'tooltip'); tip.hidden = true;
  document.body.appendChild(tip);
  var cur = null, timer = null;
  function fill(el) {
    var t = el.getAttribute('data-tip'); if (!t) return false;
    var ti = el.getAttribute('data-tip-title');
    tip.textContent = '';
    if (ti) { var s = document.createElement('strong'); s.textContent = ti; tip.appendChild(s); }
    tip.appendChild(document.createTextNode(t));
    return true;
  }
  function place(x, y) {
    var w = tip.offsetWidth, h = tip.offsetHeight;
    var nx = x + 16, ny = y + 20;
    if (nx + w > window.innerWidth - 8) nx = x - w - 16;
    if (ny + h > window.innerHeight - 8) ny = y - h - 20;
    tip.style.left = Math.max(8, nx) + 'px'; tip.style.top = Math.max(8, ny) + 'px';
  }
  function hideTip() { clearTimeout(timer); tip.hidden = true; if (cur) { cur.removeAttribute('aria-describedby'); cur = null; } }
  document.addEventListener('mouseover', function (e) {
    var el = e.target.closest ? e.target.closest('[data-tip]') : null;
    if (!el || el === cur) return;
    hideTip(); cur = el; var x = e.clientX, y = e.clientY;
    timer = setTimeout(function () { if (cur === el && fill(el)) { tip.hidden = false; el.setAttribute('aria-describedby', 'tip'); place(x, y); } }, 220);
  });
  document.addEventListener('mousemove', function (e) { if (cur && !tip.hidden) place(e.clientX, e.clientY); else if (cur) { cur._x = e.clientX; } });
  document.addEventListener('mouseout', function (e) { if (cur && (!e.relatedTarget || !cur.contains(e.relatedTarget))) hideTip(); });
  document.addEventListener('focusin', function (e) {
    var el = e.target.closest ? e.target.closest('[data-tip]') : null;
    if (!el) return; hideTip(); cur = el;
    if (fill(el)) { tip.hidden = false; el.setAttribute('aria-describedby', 'tip'); var r = el.getBoundingClientRect(); place(r.left, r.bottom - 14); }
  });
  document.addEventListener('focusout', hideTip);
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') hideTip(); });
  window.addEventListener('scroll', hideTip, { passive: true });


  // feedback dialog
  var dlg = document.getElementById('fb');
  function mail() {
    if (!dlg) return;
    var body = (d.tMailBody || '').replace('{title}', dlg.dataset.page).replace('{ref}', dlg.dataset.ref).replace('{url}', location.href);
    dlg.querySelectorAll('a[data-mail]').forEach(function (a) {
      var addr = a.getAttribute('href').split('?')[0];
      a.setAttribute('href', addr + '?subject=' + encodeURIComponent(dlg.dataset.subject) + '&body=' + encodeURIComponent(body));
    });
  }
  document.querySelectorAll('[data-dialog]').forEach(function (b) {
    b.addEventListener('click', function () { mail(); if (dlg && dlg.showModal) dlg.showModal(); });
  });
  if (dlg) dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });
})();

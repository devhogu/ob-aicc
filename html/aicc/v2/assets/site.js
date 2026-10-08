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

  // expand a diagram to its natural size
  document.querySelectorAll('.dz-open').forEach(function (b) {
    b.addEventListener('click', function () {
      var fig = b.closest('figure'); if (!fig) return;
      var old = document.getElementById('dz'); if (old) old.remove();
      var dz = document.createElement('dialog'); dz.id = 'dz'; dz.className = 'dz';
      var bar = document.createElement('div'); bar.className = 'dz-bar';
      var cap = fig.querySelector('figcaption'); var span = document.createElement('span'); span.textContent = cap ? cap.textContent : ''; bar.appendChild(span);
      var close = document.createElement('button'); close.type = 'button'; close.className = 'oc-button'; close.textContent = d.tDzClose || 'Close'; close.addEventListener('click', function () { dz.close(); }); bar.appendChild(close);
      dz.appendChild(bar);
      fig.querySelectorAll('.mm').forEach(function (m) {
        var c = m.cloneNode(true); var svg = c.querySelector('svg');
        if (svg) { var vb = (svg.getAttribute('viewBox') || '').split(/\s+/); if (vb.length === 4) { svg.style.width = Math.ceil(parseFloat(vb[2])) + 'px'; svg.style.height = 'auto'; } }
        dz.appendChild(c);
      });
      dz.addEventListener('click', function (e) { if (e.target === dz) dz.close(); });
      dz.addEventListener('close', function () { dz.remove(); b.focus(); });
      document.body.appendChild(dz); dz.showModal();
    });
  });


  // live boards: search and filters, and a card opens in place
  document.querySelectorAll('[data-kanban-workspace]').forEach(function (root) {
    var search = root.querySelector('[data-kb-search]'), selects = root.querySelectorAll('[data-kb-filter]'), count = root.querySelector('[data-kb-count]');
    var panel = root.querySelector('[data-kb-panel]'), opener = null;
    function apply() {
      var q = (search && search.value || '').toLowerCase().trim(), shown = 0;
      root.querySelectorAll('[data-kb-open], [data-kb-row]').forEach(function (el) {
        var ok = !q || (el.dataset.find || '').indexOf(q) >= 0;
        selects.forEach(function (s) { if (s.value && el.dataset[s.dataset.kbFilter] !== s.value) ok = false; });
        el.hidden = !ok;
        if (ok && el.hasAttribute('data-kb-open')) shown++;
      });
      root.querySelectorAll('.kb-column').forEach(function (col) {
        var n = col.querySelectorAll('[data-kb-open]:not([hidden])').length, c = col.querySelector('.kb-count'); if (c) c.textContent = n;
      });
      if (count) count.textContent = 'Показано: ' + shown;
      if (opener && opener.hidden) close();
    }
    function close(focus) {
      if (!panel) return; panel.hidden = true; panel.querySelector('.kb-detail-body').replaceChildren();
      if (opener) { opener.removeAttribute('aria-current'); if (focus) opener.focus(); } opener = null;
    }
    if (search) search.addEventListener('input', apply);
    selects.forEach(function (s) { s.addEventListener('change', apply); });
    root.querySelectorAll('[data-kb-open]').forEach(function (card) {
      card.addEventListener('click', function (ev) {
        if (!panel || ev.ctrlKey || ev.metaKey || ev.shiftKey || ev.button !== 0) return;
        var tpl = root.querySelector('template[data-kb-detail="' + card.dataset.kbOpen + '"]'); if (!tpl) return;
        ev.preventDefault(); close(); opener = card; card.setAttribute('aria-current', 'true');
        panel.querySelector('.kb-detail-body').replaceChildren(tpl.content.cloneNode(true));
        panel.querySelector('[data-kb-identity]').textContent = card.dataset.kbOpen;
        panel.querySelector('[data-kb-full]').href = card.href;
        panel.hidden = false; panel.scrollIntoView({block: 'nearest', behavior: 'smooth'});
      });
    });
    root.querySelectorAll('[data-kb-close]').forEach(function (b) { b.addEventListener('click', function () { close(true); }); });
    root.addEventListener('keydown', function (ev) { if (ev.key === 'Escape') close(true); });
  });
})();

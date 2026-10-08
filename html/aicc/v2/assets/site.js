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



  // accordion kanban: one column open at a time; a click on a narrow column, or on a card in it, opens that column
  document.querySelectorAll('[data-kb-accordion]').forEach(function (board) {
    var cols = Array.prototype.slice.call(board.querySelectorAll('[data-kb-column]'));
    function open(col) { cols.forEach(function (c) { c.classList.toggle('is-open', c === col); }); }
    cols.forEach(function (col) {
      var head = col.querySelector('.kb-column-head');
      head.addEventListener('click', function () { open(col); });
      head.addEventListener('keydown', function (ev) { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); open(col); } });
      col.querySelectorAll('[data-kb-open]').forEach(function (card) {
        card.addEventListener('click', function (ev) {
          if (!col.classList.contains('is-open')) { ev.preventDefault(); ev.stopImmediatePropagation(); open(col); }
        }, true);
      });
    });
    open(cols.filter(function (c) { return c.querySelector('[data-kb-open]'); })[0] || cols[0]);
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
      });
      // the count follows the open view: cards on a board, otherwise rows of a table
      var view = root.querySelector('[data-tab-panel]:not([hidden])') || root;
      shown = view.querySelectorAll('[data-kb-open]:not([hidden])').length || view.querySelectorAll('[data-kb-row]:not([hidden])').length;
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
    root.addEventListener('kb-refresh', apply);
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

  // tabs: one view at a time; without the script every view stays visible
  document.querySelectorAll('[data-tabs]').forEach(function (root) {
    var buttons = root.querySelectorAll('[data-tab]'), panels = root.querySelectorAll('[data-tab-panel]');
    root.classList.add('tabs-on');
    var keys = Array.prototype.map.call(buttons, function (b) { return b.dataset.tab; });
    function show(key) {
      buttons.forEach(function (b) { b.setAttribute('aria-selected', String(b.dataset.tab === key)); });
      panels.forEach(function (p) { p.hidden = p.dataset.tabPanel !== key; });
      root.dispatchEvent(new Event('kb-refresh', {bubbles: true}));
    }
    // a tab opens from the address (#plan) and keeps it, so a view can be linked to
    function fromHash() { var k = decodeURIComponent(location.hash.slice(1)); if (keys.indexOf(k) >= 0) { show(k); return true; } return false; }
    buttons.forEach(function (b) { b.addEventListener('click', function () { show(b.dataset.tab); try { history.replaceState(null, '', '#' + b.dataset.tab); } catch (e) {} }); });
    window.addEventListener('hashchange', fromHash);
    if (!fromHash()) show(keys[0]);
  });
  // PI calendar: the same rules as aicc/v2/tools/cadence.py, applied to the reader's date on every load
  var PI = (function () {
    var DAY = 864e5, WEEK = 7 * DAY;
    var MONTHS = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь'];
    var SHORT = ['янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек'];
    var LONG = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'];
    var DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'];
    var STATE_CLASS = {'Бэклог': 'backlog', 'Готово к работе': 'ready', 'В работе': 'doing', 'На проверке': 'review', 'Завершено': 'done'};
    var data = {days: {}, year_end_from: [12, 21], seasons: [], rows: []};
    function at(y, m, d) { return Date.UTC(y, m - 1, d); }
    function parts(t) { var x = new Date(t); return {y: x.getUTCFullYear(), m: x.getUTCMonth() + 1, d: x.getUTCDate(), wd: (x.getUTCDay() + 6) % 7}; }
    function iso(t) { var p = parts(t); return p.y + '-' + (p.m < 10 ? '0' : '') + p.m + '-' + (p.d < 10 ? '0' : '') + p.d; }
    function fromIso(s) { var p = s.split('-').map(Number); return at(p[0], p[1], p[2] || 1); }
    function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
    function cls() { var n = Array.prototype.filter.call(arguments, Boolean); return n.length ? ' class="' + n.join(' ') + '"' : ''; }
    function firstMonday(y, m) { var t = at(y, m, 1); return t + ((3 - parts(t).wd + 7) % 7) * DAY - 3 * DAY; }
    function iteration(y, m) {
      var s = firstMonday(y, m), n = firstMonday(y + (m === 12 ? 1 : 0), m % 12 + 1);
      return {name: 'I' + (m < 10 ? '0' : '') + m, label: 'i' + (m < 10 ? '0' : '') + m, month: m, year: y, pi: y + '-PIQ' + (Math.floor((m - 1) / 3) + 1), start: s, end: n - DAY, weeks: Math.round((n - s) / WEEK), title: MONTHS[m - 1]};
    }
    function itKey(i) { return i.year + '-' + (i.month < 10 ? '0' : '') + i.month; }
    function weekOf(t) {
      var monday = t - parts(t).wd * DAY, th = parts(monday + 3 * DAY), it = iteration(th.y, th.m);
      return [it, Math.round((monday - it.start) / WEEK) + 1];
    }
    // what kind of day a date is for planning: 'off', 'away' (people likely absent), 'short' or ''
    function dayKind(t) {
      var k = data.days[iso(t)]; if (k) return k;
      var p = parts(t); return p.wd < 5 && p.m === data.year_end_from[0] && p.d >= data.year_end_from[1] ? 'away' : '';
    }
    function lostDays(monday) { var n = 0; for (var k = 0; k < 5; k++) { var d = dayKind(monday + k * DAY); if (d === 'off' || d === 'away') n++; } return n; }
    function weekNote(monday) {
      var groups = {off: [], away: [], short: []};
      for (var k = 0; k < 5; k++) { var t = monday + k * DAY, d = dayKind(t), p = parts(t); if (d) groups[d].push(p.d + ' ' + SHORT[p.m - 1]); }
      var out = [['off', 'нерабочие'], ['away', 'вероятны отсутствия'], ['short', 'сокращённый день']].filter(function (g) { return groups[g[0]].length; })
        .map(function (g) { return g[1] + ': ' + (groups[g[0]].length === 5 ? 'вся неделя' : groups[g[0]].join(', ')); });
      var friday = iso(monday + 4 * DAY), mon = iso(monday);
      data.seasons.forEach(function (s) { if (s.from <= friday && mon <= s.to) out.push(s.text); });
      return out.join('; ');
    }
    function increment(y, q) {
      var its = [1, 2, 3].map(function (k) { return iteration(y, 3 * (q - 1) + k); }), last = its[2], name = y + '-PIQ' + q;
      var ipWeek = last.weeks;
      while (ipWeek > 1 && lostDays(last.start + (ipWeek - 1) * WEEK) > 2) ipWeek--;  // Planning moves to the week before until enough people are there
      var ipStart = last.start + (ipWeek - 1) * WEEK;
      return {name: name, iterations: its, start: its[0].start, end: last.end, ip: {name: name + ' ' + last.name + 'W' + ipWeek, start: ipStart, end: ipStart + 4 * DAY}};
    }
    function piByName(name) { var m = /^(\d{4})-PIQ(\d)$/.exec(name); return increment(+m[1], +m[2]); }
    function qIndex(name) { var m = /^(\d{4})-PIQ(\d)$/.exec(name); return +m[1] * 4 + +m[2] - 1; }
    function span(a, b, long) {
      var x = parts(a), y = parts(b), n = long ? LONG : SHORT;
      return x.d + ' ' + n[x.m - 1] + (x.y !== y.y ? ' ' + x.y : '') + ' – ' + y.d + ' ' + n[y.m - 1] + ' ' + y.y;
    }
    function today() { var n = new Date(); return at(n.getFullYear(), n.getMonth() + 1, n.getDate()); }
    function item(x) {
      return '<a class="pi-item pi-item--' + (STATE_CLASS[x.state] || 'backlog') + '" href="' + esc(x.href) + '" data-item="' + esc(x.id) + '" title="' + esc(x.title) + ' · ' + esc(x.state) + '"><b>' + esc(x.id) + '</b><span>' + esc(x.title) + '</span></a>';
    }
    function board(pi, it, sel) {
      var names = pi.iterations.map(function (i) { return pi.name + ' ' + i.name; });
      var head = pi.iterations.map(function (i) {
        return '<th' + cls(itKey(i) === itKey(it) ? 'is-current' : '', itKey(i) === itKey(sel) ? 'is-selected' : '') + ' data-it="' + itKey(i) + '" tabindex="0"><b>' + i.label + '</b> ' + i.title + '<small>' + span(i.start, i.end) + '</small></th>';
      }).join('');
      var body = [];
      data.rows.forEach(function (row) {
        var cells = names.map(function (n) { return row.items.filter(function (x) { return x.iteration === n; }); });
        var loose = row.items.filter(function (x) { return !x.iteration && x.state !== 'Завершено'; });
        if (!cells.some(function (c) { return c.length; }) && !loose.length) return;
        body.push('<tr data-kb-row data-find="' + esc(row.find) + '" data-function="' + esc(row['function']) + '" data-area="' + esc(row.area) + '"><th scope="row"><a href="' + esc(row.href) + '">' + esc(row.id) + '</a><span>' + esc(row.title) + '</span></th>' +
          cells.map(function (c, k) { return '<td' + cls(itKey(pi.iterations[k]) === itKey(sel) ? 'is-selected' : '') + '>' + c.map(item).join('') + '</td>'; }).join('') + '<td class="pi-loose">' + loose.map(item).join('') + '</td></tr>');
      });
      if (!body.length) body.push('<tr><td colspan="5" class="pi-empty">В этом PI работы не запланировано.</td></tr>');
      return '<div class="o-table-wrap pi-board-wrap"><table class="pi-board"><thead><tr><th>Проект</th>' + head + '<th>Не запланировано</th></tr></thead><tbody>' + body.join('') + '</tbody></table></div>';
    }
    function short(a, b) { var x = parts(a), y = parts(b); return x.m === y.m ? x.d + '–' + y.d + ' ' + SHORT[y.m - 1] : x.d + ' ' + SHORT[x.m - 1] + ' – ' + y.d + ' ' + SHORT[y.m - 1]; }
    var TAG = {ip: 'Planning', review: 'Review'};
    function weekKind(i, w, ip) {
      if (i.pi + ' ' + i.name + 'W' + w === ip) return 'ip';
      return w === i.weeks && i.month % 3 ? 'review' : '';
    }
    function quiet(s, kind) { return !kind && lostDays(s) > 2; }
    function wtext(prefix, s, kind) { return prefix + ' · ' + weekRange(s, kind) + (kind ? ' · ' + TAG[kind] : '') + (quiet(s, kind) ? ' · вероятны отсутствия' : ''); }
    function weekRange(s, kind) { return short(s, s + (kind === 'ip' ? 4 : 6) * DAY); }
    function here(day) {
      var w = weekOf(day), it = w[0], week = w[1], pi = increment(it.year, Math.floor((it.month - 1) / 3) + 1), p = parts(day);
      var monday = day - p.wd * DAY, piWeeks = Math.round((pi.end - pi.start + DAY) / WEEK), piWeek = Math.round((monday - pi.start) / WEEK) + 1, ip = pi.ip.name;
      function pick(text, now) { return esc(text + (now ? ' · сейчас' : '')); }
      var segs = pi.iterations.map(function (i) {
        var cells = '';
        for (var n = 1; n <= i.weeks; n++) {
          var s = i.start + (n - 1) * WEEK, k = weekKind(i, n, ip), text = wtext(i.label + ' W' + n, s, k);
          cells += '<button type="button"' + cls(s < monday ? 'is-done' : s === monday ? 'is-current' : '', k ? 'is-' + k : '', quiet(s, k) ? 'is-quiet' : '', s === monday ? 'is-picked' : '') +
            ' data-here-week data-range="' + pick(text, s === monday) + '" aria-label="' + i.label + ' W' + n + '"></button>';
        }
        var cur = itKey(i) === itKey(it);
        return '<li' + cls(cur ? 'is-current' : '', i.end < monday ? 'is-done' : '', cur ? 'is-picked' : '') + ' data-here-it="' + itKey(i) + '" style="flex:' + i.weeks + '"><span class="here-cells">' + cells + '</span>' +
          '<button type="button" class="here-it" data-here-week data-range="' + i.label + ' · ' + short(i.start, i.end) + ' · ' + i.weeks + ' нед."><b>' + i.label + ' · ' + i.title + '</b><span>' + short(i.start, i.end) + '</span></button></li>';
      }).join('');
      var now = weekKind(it, week, ip);
      return '<div class="here-tile" data-week="' + iso(monday) + '" tabindex="0"><small>Сегодня</small><strong>' + p.d + ' ' + LONG[p.m - 1] + ' ' + p.y + '</strong><span>' + DAYS[p.wd] + '</span></div>' +
        '<div class="here-tile" data-pi="' + pi.name + '" tabindex="0"><small>Программный инкремент · неделя ' + piWeek + ' из ' + piWeeks + '</small><div class="here-head"><strong>PI ' + pi.name + '</strong><span>' + span(pi.start, pi.end) + '</span></div>' +
        '<ol class="here-pi">' + segs + '</ol>' +
        '<span class="here-range" data-here-range>' + pick(wtext(it.label + ' W' + week, monday, now), true) + '</span>' +
        '</div>' +
        iterTile(it, day, null);
    }
    // the iteration tile for any iteration; pick is the Monday of the week to show, or null for today's week (or the first)
    function iterTile(i, day, pick) {
      var w = weekOf(day), cur = itKey(i) === itKey(w[0]), monday = day - parts(day).wd * DAY, ip = increment(i.year, Math.floor((i.month - 1) / 3) + 1).ip.name;
      if (pick === null) pick = cur ? monday : i.start;
      function text(n, s) { return esc(wtext('W' + n, s, weekKind(i, n, ip)) + (s === monday ? ' · сейчас' : '')); }
      var weeks = '', shown = '';
      for (var n = 1; n <= i.weeks; n++) {
        var s = i.start + (n - 1) * WEEK, k = weekKind(i, n, ip);
        weeks += '<li><button type="button"' + cls(s < monday ? 'is-done' : s === monday ? 'is-current' : '', k ? 'is-' + k : '', quiet(s, k) ? 'is-quiet' : '', s === pick ? 'is-picked' : '') +
          ' data-here-week data-range="' + text(n, s) + '">' + (k ? TAG[k] : 'W' + n) + '</button></li>';
        if (s === pick) shown = text(n, s);
      }
      return '<div class="here-tile" data-it="' + itKey(i) + '" tabindex="0"><small>Итерация · ' + (cur ? 'неделя ' + w[1] + ' из ' + i.weeks : i.weeks + ' нед.') + '</small><div class="here-head"><strong>' + i.label + ' · ' + i.title + '</strong><span>' + span(i.start, i.end) + '</span></div>' +
        '<ol class="here-weeks">' + weeks + '</ol><span class="here-range" data-here-range>' + shown + '</span></div>';
    }
    function iterTileOf(key, day, n) { var p = key.split('-').map(Number), i = iteration(p[0], p[1]); return iterTile(i, day, n ? i.start + (n - 1) * WEEK : null); }
    // state: {pi, it} - the increment and iteration picked by the reader; empty means today's
    function calendar(day, shift, state) {
      state = state || {};
      var w = weekOf(day), it = w[0], week = w[1], year = it.year, quarter = Math.floor((it.month - 1) / 3) + 1, q = year * 4 + quarter - 1 + shift;
      var pis = [0, 1, 2].map(function (k) { return increment(Math.floor((q + k) / 4), (q + k) % 4 + 1); });
      var shown = pis.filter(function (p) { return p.name === state.pi; })[0] || pis[0];
      var sel = shown.iterations.filter(function (i) { return itKey(i) === state.it; })[0] || (it.pi === shown.name ? it : shown.iterations[0]);
      var monday = it.start + (week - 1) * WEEK, note = weekNote(monday);
      var out = ['<div class="pi-bar"><div class="pi-now" data-week="' + iso(monday) + '" tabindex="0"><span class="pi-now__label">Сейчас</span><strong>' + it.pi + ' · ' + it.label + ' · неделя ' + week + ' из ' + it.weeks + '</strong><span>' + span(monday, monday + 6 * DAY) + '</span>' +
        (note ? '<span class="pi-note">' + esc(note) + '</span>' : '') + '</div>' +
        '<div class="pi-nav"><button type="button" data-pi-step="-1" aria-label="Предыдущий PI">‹</button><button type="button" data-pi-step="0">Сегодня</button><button type="button" data-pi-step="1" aria-label="Следующий PI">›</button></div></div><div class="pi-row">'];
      pis.forEach(function (pi) {
        var total = Math.round((pi.end - pi.start) / DAY) + 1, done = Math.max(0, Math.min(total, Math.round((day - pi.start) / DAY) + 1)), pct = Math.floor(100 * done / total);
        var st = pi.name === it.pi ? 'идёт' : (done === total ? 'завершён' : 'впереди');
        var its = pi.iterations.map(function (i) {
          return '<li' + cls(itKey(i) === itKey(it) ? 'is-current' : '', itKey(i) === itKey(sel) ? 'is-selected' : '') + ' data-it="' + itKey(i) + '" tabindex="0"><b>' + i.label + '</b><em>' + i.title + '</em><span>' + span(i.start, i.end) + ' · ' + i.weeks + ' нед.</span></li>';
        }).join('');
        out.push('<article' + cls('pi-card', pi.name === it.pi ? 'is-current' : '', pi.name === shown.name ? 'is-selected' : '') + ' data-pi="' + pi.name + '" tabindex="0">' +
          '<header><strong>' + pi.name + '</strong><small>' + st + '</small></header><span class="pi-dates">' + span(pi.start, pi.end) + '</span>' +
          '<div class="pi-progress" title="Пройдено ' + pct + '%"><span style="width:' + pct + '%"></span></div>' +
          '<ol class="pi-its">' + its + '</ol><p class="pi-ip"><b>Planning</b> ' + span(pi.ip.start, pi.ip.end) + '</p></article>');
      });
      out.push('</div>');
      var weeks = [];
      for (var n = 1; n <= sel.weeks; n++) {
        var start = sel.start + (n - 1) * WEEK, name = sel.pi + ' ' + sel.name + 'W' + n, text = weekNote(start);
        weeks.push('<li' + cls(start === monday ? 'is-current' : '', name === shown.ip.name ? 'is-ip' : '', weekKind(sel, n, shown.ip.name) === 'review' ? 'is-review' : '') + ' data-week="' + iso(start) + '" tabindex="0"><b>W' + n + '</b><span>' + span(start, start + 6 * DAY) + '</span>' + (text ? '<small>' + esc(text.split(';')[0]) + '</small>' : '') + '</li>');
      }
      out.push('<div class="pi-weeks"><span class="pi-weeks__label">Недели итерации ' + sel.label + ' (' + sel.title + ') · нажмите на неделю, итерацию или PI, чтобы открыть подробности</span><ol>' + weeks.join('') + '</ol></div>' +
        '<h3 class="pi-board-title">Работа по итерациям ' + shown.name + '</h3>' + board(shown, it, sel));
      return out.join('');
    }

    // pop-up content: what a PI, an iteration, a week or a work item holds
    function work(names) {
      var list = [];
      data.rows.forEach(function (row) { row.items.forEach(function (x) { if (names.indexOf(x.iteration) >= 0) list.push(x); }); });
      return list;
    }
    function itemList(list, empty) {
      return list.length ? '<div class="pop-items">' + list.map(item).join('') + '</div>' : '<p class="pop-muted">' + empty + '</p>';
    }
    function popPI(name, day) {
      var pi = piByName(name), it = weekOf(day)[0], weeks = Math.round((pi.end - pi.start + DAY) / WEEK);
      var total = Math.round((pi.end - pi.start) / DAY) + 1, done = Math.max(0, Math.min(total, Math.round((day - pi.start) / DAY) + 1));
      var rows = pi.iterations.map(function (i) {
        var n = work([pi.name + ' ' + i.name]).length;
        return '<li' + cls(itKey(i) === itKey(it) ? 'is-current' : '') + ' data-it="' + itKey(i) + '" tabindex="0"><b>' + i.label + '</b><span>' + i.title + '</span><span>' + span(i.start, i.end) + '</span><span>' + i.weeks + ' нед.</span><span>' + (n ? 'работ: ' + n : '—') + '</span></li>';
      }).join('');
      var marked = [];
      for (var t = pi.start; t <= pi.end; t += WEEK) { var note = weekNote(t); if (note) marked.push('<li data-week="' + iso(t) + '" tabindex="0"><b>' + span(t, t + 6 * DAY) + '</b><span>' + esc(note) + '</span></li>'); }
      return '<header><small>Программный инкремент · ' + (pi.name === it.pi ? 'идёт' : done === total ? 'завершён' : 'впереди') + '</small><h2>PI ' + pi.name + '</h2><p>' + span(pi.start, pi.end, true) + ' · ' + weeks + ' недель</p>' +
        '<div class="pi-progress"><span style="width:' + Math.floor(100 * done / total) + '%"></span></div></header>' +
        '<h3>Итерации</h3><ul class="pop-rows pop-rows--its">' + rows + '</ul>' +
        '<h3>Planning</h3><p>' + span(pi.ip.start, pi.ip.end, true) + ': ревью и демонстрация третьей итерации, инновации и планирование следующего PI.</p>' +
        '<h3>Отмеченные недели</h3>' + (marked.length ? '<ul class="pop-rows">' + marked.join('') + '</ul>' : '<p class="pop-muted">Отметок нет.</p>') +
        '<h3>Работа в этом PI</h3>' + itemList(work(pi.iterations.map(function (i) { return pi.name + ' ' + i.name; })), 'В этот PI работа пока не запланирована.');
    }
    function popIt(key, day) {
      var p = key.split('-').map(Number), i = iteration(p[0], p[1]), w = weekOf(day), monday = day - parts(day).wd * DAY, ip = piByName(i.pi).ip.name, weeks = [];
      for (var n = 1; n <= i.weeks; n++) {
        var s = i.start + (n - 1) * WEEK, note = weekNote(s);
        weeks.push('<li' + cls(s === monday ? 'is-current' : '', i.pi + ' ' + i.name + 'W' + n === ip ? 'is-ip' : '', weekKind(i, n, ip) === 'review' ? 'is-review' : '') + ' data-week="' + iso(s) + '" tabindex="0"><b>W' + n + '</b><span>' + span(s, s + 6 * DAY) + '</span><span>' + (esc(note) || '—') + '</span></li>');
      }
      return '<header><small>Итерация · PI <a href="#" data-pi="' + i.pi + '">' + i.pi + '</a>' + (itKey(i) === itKey(w[0]) ? ' · идёт, неделя ' + w[1] : '') + '</small><h2>' + i.label + ' · ' + i.title + ' ' + i.year + '</h2><p>' + span(i.start, i.end, true) + ' · ' + i.weeks + ' нед.</p></header>' +
        '<h3>Недели</h3><ul class="pop-rows pop-rows--weeks">' + weeks.join('') + '</ul>' +
        '<h3>Работа в этой итерации</h3>' + itemList(work([i.pi + ' ' + i.name]), 'В эту итерацию работа пока не запланирована.');
    }
    function popWeek(key, day) {
      var start = fromIso(key), w = weekOf(start), i = w[0], events = [];
      var friday = iso(start + 4 * DAY), mon = iso(start);
      data.seasons.forEach(function (s) { if (s.from <= friday && mon <= s.to) events.push(s.text); });
      var kind = weekKind(i, w[1], piByName(i.pi).ip.name);
      if (kind) events.unshift(TAG[kind]);
      var days = [];
      for (var k = 0; k < 7; k++) {
        var t = start + k * DAY, p = parts(t), dk = k < 5 ? dayKind(t) : '';
        days.push('<li' + cls(k > 4 ? 'is-weekend' : '', dk ? 'is-' + dk : '', t === day ? 'is-today' : '') + '><small>' + DAYS[k].slice(0, 2) + '</small><b>' + p.d + '</b><span>' + SHORT[p.m - 1] + '</span></li>');
      }
      return '<header><small>Неделя ' + w[1] + ' из ' + i.weeks + ' · итерация <a href="#" data-it="' + itKey(i) + '">' + i.label + ' ' + i.title + '</a> · PI <a href="#" data-pi="' + i.pi + '">' + i.pi + '</a></small><h2>W' + w[1] + ' · ' + span(start, start + 6 * DAY) + '</h2>' +
        (events.length ? '<p class="pop-events">' + events.map(function (e) { return '<span>' + esc(e) + '</span>'; }).join('') + '</p>' : '') + '</header>' +
        '<ol class="pop-days">' + days.join('') + '</ol>' +
        '<p class="pop-legend"><span class="is-off">нерабочий день</span><span class="is-short">сокращённый день</span><span class="is-away">вероятны отсутствия</span><span class="is-today">сегодня</span></p>' +
        '<h3>Работа в итерации ' + i.label + '</h3>' + itemList(work([i.pi + ' ' + i.name]), 'В эту итерацию работа пока не запланирована.');
    }
    function popItem(id) {
      var found = null, card = null;
      data.rows.forEach(function (row) { row.items.forEach(function (x) { if (x.id === id) { found = x; card = row; } }); });
      if (!found) return '<p class="pop-muted">Не найдено.</p>';
      var tpl = document.querySelector('template[data-kb-detail="' + card.id + '"]'), wrap = document.createElement('div');
      if (tpl) wrap.appendChild(tpl.content.cloneNode(true));
      var planned = found.iteration ? 'итерация <a href="#" data-it="' + found.iteration.slice(0, 4) + '-' + found.iteration.slice(11, 13) + '">' + esc(found.iteration.replace(' I', ' i')) + '</a>' : 'ещё не запланировано';
      return '<header><small>' + esc(found.id) + ' · ' + esc(found.state) + ' · ' + planned + '</small><h2>' + esc(found.title) + '</h2></header>' +
        '<h3>Проект ' + esc(card.id) + '</h3><div class="pop-card">' + wrap.innerHTML + '</div>' +
        '<p><a class="pop-full" href="' + esc(card.href) + '">Полная карточка проекта →</a></p>';
    }
    function pop(kind, key, day) {
      return kind === 'pi' ? popPI(key, day) : kind === 'it' ? popIt(key, day) : kind === 'week' ? popWeek(key, day) : popItem(key);
    }
    return {data: data, today: today, at: at, here: here, iterTileOf: iterTileOf, calendar: calendar, pop: pop, qIndex: qIndex, weekOf: weekOf, fromIso: fromIso, itKey: itKey};
  })();
  window.HubPI = PI;

  // the explorer: a click on a PI, an iteration, a week or a work item selects it and opens its details; inside, the same clicks go deeper
  document.querySelectorAll('[data-pi-calendar]').forEach(function (el) {
    try { var given = JSON.parse(el.dataset.piCalendar); PI.data.days = given.days || {}; PI.data.year_end_from = given.year_end_from || [12, 21]; PI.data.seasons = given.seasons || []; PI.data.rows = given.rows || []; } catch (e) {}
    var day = PI.today(), shift = 0, state = {}, dlg = null, stack = [], opener = null;
    var base = PI.qIndex(PI.weekOf(day)[0].pi);
    function draw() { el.innerHTML = PI.calendar(day, shift, state); el.dispatchEvent(new Event('kb-refresh', {bubbles: true})); }
    function select(kind, key) {
      var pi = kind === 'pi' ? key : kind === 'it' ? PI.weekOf(PI.fromIso(key + '-15'))[0].pi : PI.weekOf(PI.fromIso(key))[0].pi;
      var q = PI.qIndex(pi);
      if (q < base + shift || q > base + shift + 2) shift = q - base;
      state = {pi: pi, it: kind === 'it' ? key : kind === 'week' ? PI.itKey(PI.weekOf(PI.fromIso(key))[0]) : null};
      draw();
    }
    function render() {
      var top = stack[stack.length - 1];
      dlg.querySelector('.pi-pop__body').innerHTML = PI.pop(top[0], top[1], day);
      dlg.querySelector('[data-pop-back]').hidden = stack.length < 2;
      dlg.querySelector('.pi-pop__body').scrollTop = 0;
    }
    function open(kind, key, deeper) {
      if (!dlg) {
        dlg = document.createElement('dialog'); dlg.className = 'pi-pop';
        dlg.innerHTML = '<div class="pi-pop__bar"><button type="button" data-pop-back>← Назад</button><button type="button" data-pop-close>Закрыть ×</button></div><div class="pi-pop__body"></div>';
        document.body.appendChild(dlg);
        dlg.addEventListener('click', function (ev) {
          if (ev.target === dlg || ev.target.closest('[data-pop-close]')) { dlg.close(); return; }
          if (ev.target.closest('[data-pop-back]')) { stack.pop(); render(); return; }
          var t = ev.target.closest('[data-item],[data-week],[data-it],[data-pi]');
          if (t && !(ev.ctrlKey || ev.metaKey || ev.shiftKey)) { ev.preventDefault(); go(t, true); }
        });
        dlg.addEventListener('keydown', function (ev) {
          var t = ev.target.closest && ev.target.closest('li[data-week],li[data-it]');
          if (t && ev.key === 'Enter') { ev.preventDefault(); go(t, true); }
        });
        dlg.addEventListener('close', function () { stack = []; if (opener && document.contains(opener)) opener.focus(); });
      }
      if (!deeper) stack = [];
      stack.push([kind, key]); render();
      if (!dlg.open) dlg.showModal();
    }
    function go(t, deeper) {
      var kind = t.hasAttribute('data-item') ? 'item' : t.hasAttribute('data-week') ? 'week' : t.hasAttribute('data-it') ? 'it' : 'pi';
      open(kind, t.getAttribute('data-' + kind), deeper);
    }
    function pick(t) {
      var kind = t.hasAttribute('data-item') ? 'item' : t.hasAttribute('data-week') ? 'week' : t.hasAttribute('data-it') ? 'it' : 'pi';
      var key = t.getAttribute('data-' + kind), inside = el.contains(t);
      opener = t;
      if (kind !== 'item') { select(kind, key); if (inside) opener = el.querySelector('[data-' + kind + '="' + key + '"]') || t; }
      open(kind, key, false);
    }
    // a tile at the top takes the reader to the same place on the plan: selected, scrolled into view and briefly lit
    function jump(t) {
      var kind = t.hasAttribute('data-week') ? 'week' : t.hasAttribute('data-it') ? 'it' : 'pi', key = t.getAttribute('data-' + kind);
      var tab = document.querySelector('[data-tab="plan"]'); if (tab) tab.click();
      select(kind, key);
      var spots = kind === 'pi' ? el.querySelectorAll('.pi-card[data-pi="' + key + '"]') : kind === 'it' ? el.querySelectorAll('[data-it="' + key + '"]') : el.querySelectorAll('.pi-weeks [data-week="' + key + '"]');
      if (!spots.length) return;
      spots[0].scrollIntoView({block: 'center', behavior: 'smooth'});
      spots.forEach(function (s) { s.classList.remove('is-flash'); void s.offsetWidth; s.classList.add('is-flash'); });
      setTimeout(function () { spots.forEach(function (s) { s.classList.remove('is-flash'); }); }, 1800);
    }
    draw();
    document.querySelectorAll('[data-pi-here]').forEach(function (h) {
      h.innerHTML = PI.here(day);
      // weeks and iterations in a tile: hovering previews one, a click keeps it; leaving returns to the kept one
      function show(wk) {
        var tile = wk.closest('.here-tile'), seg = wk.closest('.here-pi > li');
        tile.querySelectorAll('[data-here-week]').forEach(function (b) { b.classList.toggle('is-picked', b.dataset.range === wk.dataset.range); });
        tile.querySelectorAll('.here-pi > li').forEach(function (li) { li.classList.toggle('is-picked', li === seg); });
        tile.querySelector('[data-here-range]').textContent = wk.dataset.range;
      }
      function under(target) {
        var wk = target.closest('[data-here-week]'); if (wk) return wk;
        var seg = target.closest('.here-pi > li'); return seg ? seg.querySelector('.here-it') : null;
      }
      var kept = new Map();
      function bind(tile) {
        var k = tile.querySelector('[data-here-week].is-picked'); if (k) kept.set(tile, k);
        tile.querySelectorAll('.here-pi, .here-weeks').forEach(function (area) {
          area.addEventListener('mouseleave', function () { if (kept.get(tile)) show(kept.get(tile)); });
        });
      }
      h.querySelectorAll('.here-tile').forEach(bind);
      h.addEventListener('mouseover', function (ev) { var wk = under(ev.target); if (wk) show(wk); });
      h.addEventListener('click', function (ev) {
        var wk = under(ev.target);
        if (wk) {  // stay on the tile; an iteration picked on the PI tile also fills the iteration tile
          kept.set(wk.closest('.here-tile'), wk); show(wk);
          var seg = wk.closest('[data-here-it]'), old = h.querySelector('.here-tile[data-it]');
          if (seg && old) {
            var cells = Array.prototype.slice.call(seg.querySelectorAll('.here-cells [data-here-week]')), n = cells.indexOf(wk) + 1;
            var box = document.createElement('div'); box.innerHTML = PI.iterTileOf(seg.dataset.hereIt, day, n || null);
            var tile = box.firstChild; old.replaceWith(tile); bind(tile);
            tile.classList.add('is-flash'); setTimeout(function () { tile.classList.remove('is-flash'); }, 900);
          }
          return;
        }
        var t = ev.target.closest('[data-week],[data-it],[data-pi]'); if (!t) return;
        jump(t);
      });
      h.addEventListener('keydown', function (ev) {
        if ((ev.key === 'Enter' || ev.key === ' ') && ev.target.classList.contains('here-tile')) { ev.preventDefault(); ev.target.click(); }
      });
    });
    el.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-pi-step]');
      if (b) {
        var step = parseInt(b.dataset.piStep, 10); shift = step ? shift + step : 0; state = {}; draw();
        var again = el.querySelector('[data-pi-step="' + b.dataset.piStep + '"]'); if (again) again.focus();
        return;
      }
      var t = ev.target.closest('[data-item],[data-week],[data-it],[data-pi]');
      if (!t || ev.ctrlKey || ev.metaKey || ev.shiftKey) return;
      ev.preventDefault(); pick(t);
    });
    el.addEventListener('keydown', function (ev) {
      if (ev.key !== 'Enter' && ev.key !== ' ') return;
      var t = ev.target.matches && ev.target.matches('[tabindex][data-week],[tabindex][data-it],[tabindex][data-pi]') ? ev.target : null;
      if (t) { ev.preventDefault(); pick(t); }
    });
  });
})();

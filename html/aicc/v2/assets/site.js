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
    var data = {ip_weeks: {}, notes: {}, rows: []};
    function at(y, m, d) { return Date.UTC(y, m - 1, d); }
    function parts(t) { var x = new Date(t); return {y: x.getUTCFullYear(), m: x.getUTCMonth() + 1, d: x.getUTCDate(), wd: (x.getUTCDay() + 6) % 7}; }
    function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
    function firstMonday(y, m) { var t = at(y, m, 1); return t + ((3 - parts(t).wd + 7) % 7) * DAY - 3 * DAY; }
    function iteration(y, m) {
      var s = firstMonday(y, m), n = firstMonday(y + (m === 12 ? 1 : 0), m % 12 + 1);
      return {name: 'I' + (m < 10 ? '0' : '') + m, month: m, year: y, pi: y + '-PIQ' + (Math.floor((m - 1) / 3) + 1), start: s, end: n - DAY, weeks: Math.round((n - s) / WEEK), title: MONTHS[m - 1]};
    }
    function weekOf(t) {
      var monday = t - parts(t).wd * DAY, th = parts(monday + 3 * DAY), it = iteration(th.y, th.m);
      return [it, Math.round((monday - it.start) / WEEK) + 1];
    }
    function increment(y, q) {
      var its = [1, 2, 3].map(function (k) { return iteration(y, 3 * (q - 1) + k); }), last = its[2], name = y + '-PIQ' + q;
      var ipWeek = last.month === 12 && last.weeks === 5 ? last.weeks - 1 : last.weeks;
      if (data.ip_weeks[name]) ipWeek = parseInt(data.ip_weeks[name].split('W').pop(), 10);
      var ipStart = last.start + (ipWeek - 1) * WEEK;
      return {name: name, iterations: its, start: its[0].start, end: last.end, ip: {name: name + ' ' + last.name + 'W' + ipWeek, start: ipStart, end: ipStart + 4 * DAY}};
    }
    function span(a, b, long) {
      var x = parts(a), y = parts(b), n = long ? LONG : SHORT;
      return x.d + ' ' + n[x.m - 1] + (x.y !== y.y ? ' ' + x.y : '') + ' – ' + y.d + ' ' + n[y.m - 1] + ' ' + y.y;
    }
    var STATE_CLASS = {'Бэклог': 'backlog', 'Готово к работе': 'ready', 'В работе': 'doing', 'На проверке': 'review', 'Завершено': 'done'};
    function item(x) {
      return '<a class="pi-item pi-item--' + (STATE_CLASS[x.state] || 'backlog') + '" href="' + esc(x.href) + '" title="' + esc(x.title) + ' · ' + esc(x.state) + '"><b>' + esc(x.id) + '</b><span>' + esc(x.title) + '</span></a>';
    }
    function board(pi, it) {
      var names = pi.iterations.map(function (i) { return pi.name + ' ' + i.name; });
      var head = pi.iterations.map(function (i) {
        return '<th' + (i.name === it.name && i.year === it.year ? ' class="is-current"' : '') + '><b>' + i.name + '</b> ' + i.title + '<small>' + span(i.start, i.end) + '</small></th>';
      }).join('');
      var body = [];
      data.rows.forEach(function (row) {
        var cells = names.map(function (n) { return row.items.filter(function (x) { return x.iteration === n; }); });
        var loose = row.items.filter(function (x) { return !x.iteration && x.state !== 'Завершено'; });
        if (!cells.some(function (c) { return c.length; }) && !loose.length) return;
        body.push('<tr data-kb-row data-find="' + esc(row.find) + '" data-function="' + esc(row['function']) + '" data-area="' + esc(row.area) + '"><th scope="row"><a href="' + esc(row.href) + '">' + esc(row.id) + '</a><span>' + esc(row.title) + '</span></th>' +
          cells.map(function (c) { return '<td>' + c.map(item).join('') + '</td>'; }).join('') + '<td class="pi-loose">' + loose.map(item).join('') + '</td></tr>');
      });
      if (!body.length) body.push('<tr><td colspan="5" class="pi-empty">В этом PI работы не запланировано.</td></tr>');
      return '<div class="o-table-wrap pi-board-wrap"><table class="pi-board"><thead><tr><th>Проект</th>' + head + '<th>Не запланировано</th></tr></thead><tbody>' + body.join('') + '</tbody></table></div>';
    }
    function today() { var n = new Date(); return at(n.getFullYear(), n.getMonth() + 1, n.getDate()); }
    var DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'];
    function here(day) {
      var w = weekOf(day), it = w[0], week = w[1], pi = increment(it.year, Math.floor((it.month - 1) / 3) + 1), p = parts(day);
      var monday = day - p.wd * DAY, piWeeks = Math.round((pi.end - pi.start + DAY) / WEEK), piWeek = Math.round((monday - pi.start) / WEEK) + 1;
      var dots = '', note = data.notes[it.pi + ' ' + it.name + 'W' + week] || '';
      for (var n = 1; n <= it.weeks; n++) dots += '<li class="' + (n < week ? 'is-done' : n === week ? 'is-current' : '') + '">W' + n + '</li>';
      return '<a class="here-tile" href="#plan"><small>Сегодня</small><strong>' + p.d + ' ' + LONG[p.m - 1] + ' ' + p.y + '</strong><span>' + DAYS[p.wd] + '</span></a>' +
        '<a class="here-tile" href="#plan"><small>Программный инкремент</small><strong>PI ' + pi.name + '</strong><span>' + span(pi.start, pi.end) + '</span>' +
        '<div class="here-bar"><i style="width:' + Math.floor(100 * piWeek / piWeeks) + '%"></i></div><span>неделя ' + piWeek + ' из ' + piWeeks + ' · неделя IP ' + span(pi.ip.start, pi.ip.end) + '</span></a>' +
        '<a class="here-tile" href="#plan"><small>Итерация</small><strong>' + it.name + ' · ' + it.title + '</strong><span>' + span(it.start, it.end) + '</span>' +
        '<ol class="here-weeks">' + dots + '</ol><span>неделя ' + week + ' из ' + it.weeks + '</span>' + (note ? '<span class="here-note">' + esc(note) + '</span>' : '') + '</a>';
    }
    function calendar(day, shift) {
      var w = weekOf(day), it = w[0], week = w[1], year = it.year, quarter = Math.floor((it.month - 1) / 3) + 1, q = year * 4 + quarter - 1 + shift;
      var monday = it.start + (week - 1) * WEEK, wname = it.pi + ' ' + it.name + 'W' + week, note = data.notes[wname] || '';
      var out = ['<div class="pi-bar"><div class="pi-now"><span class="pi-now__label">Сейчас</span><strong>' + it.pi + ' · ' + it.name + ' · неделя ' + week + ' из ' + it.weeks + '</strong><span>' + span(monday, monday + 6 * DAY) + '</span>' +
        (note ? '<span class="pi-note">' + esc(note) + '</span>' : '') + '</div>' +
        '<div class="pi-nav"><button type="button" data-pi-step="-1" aria-label="Предыдущий PI">‹</button><button type="button" data-pi-step="0">Сегодня</button><button type="button" data-pi-step="1" aria-label="Следующий PI">›</button></div></div><div class="pi-row">'];
      var pis = [0, 1, 2].map(function (k) { return increment(Math.floor((q + k) / 4), (q + k) % 4 + 1); });
      for (var k = 0; k < 3; k++) {
        var pi = pis[k];
        var total = Math.round((pi.end - pi.start) / DAY) + 1, done = Math.max(0, Math.min(total, Math.round((day - pi.start) / DAY) + 1)), pct = Math.floor(100 * done / total);
        var state = pi.name === it.pi ? 'идёт' : (done === total ? 'завершён' : 'впереди');
        var rows = pi.iterations.map(function (i) {
          return '<li' + (i.name === it.name && i.year === it.year ? ' class="is-current"' : '') + '><b>' + i.name + '</b><em>' + i.title + '</em><span>' + span(i.start, i.end) + ' · ' + i.weeks + ' нед.</span></li>';
        }).join('');
        out.push('<article class="pi-card' + (pi.name === it.pi ? ' is-current' : '') + '"><header><strong>' + pi.name + '</strong><small>' + state + '</small></header>' +
          '<span class="pi-dates">' + span(pi.start, pi.end) + '</span><div class="pi-progress" title="Пройдено ' + pct + '%"><span style="width:' + pct + '%"></span></div>' +
          '<ol class="pi-its">' + rows + '</ol><p class="pi-ip"><b>Неделя IP</b> ' + span(pi.ip.start, pi.ip.end) + '</p></article>');
      }
      out.push('</div>');
      var ip = increment(year, quarter).ip.name, weeks = [];
      for (var n = 1; n <= it.weeks; n++) {
        var start = it.start + (n - 1) * WEEK, name = it.pi + ' ' + it.name + 'W' + n, text = data.notes[name] || '';
        var cls = [n === week ? 'is-current' : '', name === ip ? 'is-ip' : ''].filter(Boolean).join(' ');
        weeks.push('<li' + (cls ? ' class="' + cls + '"' : '') + (text ? ' title="' + esc(text) + '"' : '') + '><b>W' + n + '</b><span>' + span(start, start + 6 * DAY) + '</span>' + (text ? '<small>' + esc(text.split(';')[0]) + '</small>' : '') + '</li>');
      }
      out.push('<div class="pi-weeks"><span class="pi-weeks__label">Недели итерации ' + it.name + ' (' + it.title + ')</span><ol>' + weeks.join('') + '</ol></div>' +
        '<h3 class="pi-board-title">Работа по итерациям ' + pis[0].name + '</h3>' + board(pis[0], it));
      return out.join('');
    }
    return {data: data, today: today, at: at, here: here, calendar: calendar};
  })();
  window.HubPI = PI;
  document.querySelectorAll('[data-pi-calendar]').forEach(function (el) {
    try { var given = JSON.parse(el.dataset.piCalendar); PI.data.ip_weeks = given.ip_weeks || {}; PI.data.notes = given.notes || {}; PI.data.rows = given.rows || []; } catch (e) {}
    var shift = 0;
    function draw() { el.innerHTML = PI.calendar(PI.today(), shift); el.dispatchEvent(new Event('kb-refresh', {bubbles: true})); }
    draw();
    document.querySelectorAll('[data-pi-here]').forEach(function (h) { h.innerHTML = PI.here(PI.today()); });
    el.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-pi-step]'); if (!b) return;
      var step = parseInt(b.dataset.piStep, 10); shift = step ? shift + step : 0; draw();
      var again = el.querySelector('[data-pi-step="' + b.dataset.piStep + '"]'); if (again) again.focus();
    });
  });
})();

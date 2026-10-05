/* Direct-file edition: carry the theme between files and handle restricted copying. */
(function () {
  'use strict';
  if (location.protocol !== 'file:') return;
  var root = document.documentElement;
  var theme = new URL(location.href).searchParams.get('theme');
  if (theme === 'dark' || theme === 'light') root.dataset.theme = theme;

  function carryTheme(event) {
    var link = event.target.closest('a[href]');
    if (!link || link.getAttribute('href').charAt(0) === '#') return;
    var url = new URL(link.href);
    if (url.protocol !== 'file:' || !url.pathname.endsWith('.html')) return;
    url.searchParams.set('theme', root.dataset.theme === 'dark' ? 'dark' : 'light');
    link.href = url.href;
  }
  document.addEventListener('click', carryTheme, true);
  document.addEventListener('auxclick', carryTheme, true);

  function manualCopy(text) {
    var ru = root.lang === 'ru';
    var dialog = document.createElement('dialog');
    dialog.setAttribute('aria-label', ru ? 'Копировать текст' : 'Copy text');
    var hint = document.createElement('p');
    hint.textContent = ru ? 'Нажмите Ctrl+C (⌘C на Mac), затем закройте окно.' : 'Press Ctrl+C (⌘C on Mac), then close this window.';
    var field = document.createElement('textarea');
    field.readOnly = true;
    field.value = text;
    field.rows = 12;
    field.style.width = 'min(70vw, 50rem)';
    field.setAttribute('aria-label', ru ? 'Текст для копирования' : 'Text to copy');
    var close = document.createElement('button');
    close.type = 'button';
    close.textContent = ru ? 'Закрыть' : 'Close';
    close.addEventListener('click', function () { dialog.close(); });
    dialog.append(hint, field, close);
    dialog.addEventListener('close', function () { dialog.remove(); });
    document.body.appendChild(dialog);
    dialog.showModal();
    field.focus();
    field.select();
  }
  function legacyCopy(text) {
    var field = document.createElement('textarea');
    field.value = text;
    field.style.position = 'fixed';
    field.style.left = '-10000px';
    document.body.appendChild(field);
    field.select();
    var copied = false;
    try { copied = document.execCommand('copy'); } catch (e) {}
    field.remove();
    if (!copied) manualCopy(text);
    return copied;
  }
  document.addEventListener('click', function (event) {
    var button = event.target.closest('[data-copy-text], [data-copy]');
    if (!button) return;
    var source = button.hasAttribute('data-copy-text') ? null : document.getElementById(button.dataset.copy);
    if (!button.hasAttribute('data-copy-text') && !source) return;
    var text = source ? source.textContent : button.dataset.copyText;
    event.preventDefault();
    event.stopImmediatePropagation();
    var copy = navigator.clipboard ? navigator.clipboard.writeText(text).then(function () { return true; }, function () { return legacyCopy(text); }) : Promise.resolve(legacyCopy(text));
    copy.then(function (copied) {
      if (!copied) return;
      var script = document.querySelector('script[data-search]');
      var label = script.dataset.tCopied;
      if (button.classList.contains('icon-copy')) {
        var title = button.title;
        button.classList.add('copied'); button.title = label;
        setTimeout(function () { button.classList.remove('copied'); button.title = title; }, 1500);
      } else {
        var before = button.textContent;
        button.textContent = label;
        setTimeout(function () { button.textContent = before; }, 1500);
      }
    });
  }, true);
})();

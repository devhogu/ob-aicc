/* Exercise the real site script at its input-event, fetch and result-link boundaries. */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

function searchPage() {
  function element(tag) {
    return {
      tag, children: [], events: {}, dataset: {}, hidden: true,
      appendChild(child) { this.children.push(child); },
      addEventListener(name, fn) { this.events[name] = fn; },
      setAttribute(name, value) { this[name] = value; },
      set innerHTML(value) { this.children = []; },
    };
  }
  const input = element('input'), results = element('div');
  const pending = [];
  const entries = [
    {u: '/ru/reference/change-history/', t: 'История изменений', h: 'История изменений', x: ''},
    {u: '/ru/reference/records-and-systems/', t: 'Записи и системы', h: 'Записи и системы', x: ''},
  ];
  const document = {
    currentScript: {dataset: {search: '../assets/search-ru.json'}},
    documentElement: {dataset: {}}, body: element('body'),
    getElementById: id => ({q: input, results})[id] || null,
    querySelector: () => null, querySelectorAll: () => [],
    createElement: element, addEventListener() {},
  };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../site/site.js'), 'utf8'), {
    document, window: {addEventListener() {}},
    fetch: () => new Promise(resolve => pending.push(() => resolve({json: async () => entries}))),
  });
  return {
    type(value) { input.value = value; input.events.input(); },
    async complete(index) { pending[index](); await new Promise(setImmediate); },
    links: () => results.children.filter(x => x.tag === 'a').map(x => x.href),
    visible: () => !results.hidden,
  };
}

test('a late search response still shows the latest Russian query', async () => {
  const page = searchPage();
  page.type('История');
  page.type('Записи и системы');
  await page.complete(1);
  assert.deepEqual(page.links(), ['../ru/reference/records-and-systems/']);
  await page.complete(0);
  assert.deepEqual(page.links(), ['../ru/reference/records-and-systems/']);
});

test('clearing the query while the index loads keeps results hidden', async () => {
  const page = searchPage();
  page.type('История');
  page.type('');
  await page.complete(0);
  assert.equal(page.visible(), false);
});

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
    {u: '/ru/reference/records-and-systems/', t: 'Учётная система', h: 'Учётная система', x: ''},
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
  page.type('Учётная система');
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

function scopedPage(checked) {
  function element(tag) {
    return {
      tag, children: [], events: {}, dataset: {}, hidden: true, textContent: '',
      appendChild(child) { this.children.push(child); },
      addEventListener(name, fn) { this.events[name] = fn; },
      setAttribute(name, value) { this[name] = value; },
      contains() { return false; },
      set innerHTML(value) { this.children = []; },
    };
  }
  const input = element('input'), results = element('div'), every = element('input');
  every.checked = checked;
  const indexes = {
    '../assets/search-center-en.json': [{u: '/en/center/reference/vocabulary/#t-kanban', t: 'Vocabulary', h: 'Kanban', x: 'A board of work'}],
    '../assets/search-portfolio-en.json': [{u: '/en/portfolio/', t: 'Portfolio', h: 'Portfolio Kanban', x: 'Initiatives on the Kanban'}],
  };
  const requested = [];
  const document = {
    currentScript: {dataset: {search: '../assets/search-center-en.json', searchAll: Object.keys(indexes).join(' '), searchNames: 'Center|Portfolio'}},
    documentElement: {dataset: {}}, body: element('body'), head: element('head'),
    getElementById: id => ({q: input, results, 'q-all': every})[id] || null,
    querySelector: () => null, querySelectorAll: () => [],
    createElement: element, addEventListener() {},
  };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../site/site.js'), 'utf8'), {
    document, window: {addEventListener() {}},
    fetch: url => { requested.push(url); return Promise.resolve({json: async () => indexes[url]}); },
  });
  return {
    async type(value) { input.value = value; input.events.input(); await new Promise(setImmediate); },
    async toggle(value) { every.checked = value; every.events.change(); await new Promise(setImmediate); },
    links: () => results.children.filter(x => x.tag === 'a').map(x => x.href),
    branches: () => results.children.filter(x => x.tag === 'a').map(x => (x.children.find(c => c.className === 'search-branch') || {}).textContent || ''),
    requested,
  };
}

test('a page searches its own branch until the global scope is on', async () => {
  const page = scopedPage(false);
  await page.type('kanban');
  assert.deepEqual(page.links(), ['../en/center/reference/vocabulary/#t-kanban']);
  assert.deepEqual(page.requested, ['../assets/search-center-en.json']);
  assert.deepEqual(page.branches(), ['']);
  await page.toggle(true);
  assert.deepEqual(page.links().sort(), ['../en/center/reference/vocabulary/#t-kanban', '../en/portfolio/']);
  assert.deepEqual(page.branches().sort(), ['Center', 'Portfolio']);
});

test('the global scope on by default searches every branch index', async () => {
  const page = scopedPage(true);
  await page.type('portfolio kanban');
  assert.deepEqual(page.links(), ['../en/portfolio/']);
  assert.deepEqual(page.branches(), ['Portfolio']);
  assert.deepEqual(page.requested, ['../assets/search-center-en.json', '../assets/search-portfolio-en.json']);
});

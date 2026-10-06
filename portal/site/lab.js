// START_MODULE_CONTRACT
//   PURPOSE: Focus the laboratory matrix without changing its content.
//   SCOPE: Progressive stage navigation, full-matrix reading and fragment visibility.
//   DEPENDS: M-PORTAL-NEIGHBOURS
//   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
//   MAP_MODE: SUMMARY
// END_MODULE_CONTRACT
// START_MODULE_MAP
//   update - focus existing matrix columns and announce the selected view
//   revealFragment - restore content visibility and focus its linked destination
// END_MODULE_MAP
(() => {
  const root = document.querySelector('.lab-content');
  if (!root) return;
  const matrix = root.querySelector('.lab-matrix');
  const controls = root.querySelector('.lab-controls');
  const stageButtons = [...controls.querySelectorAll('[data-lab-stage]')];
  const viewButtons = [...controls.querySelectorAll('[data-lab-view]')];
  const stages = stageButtons.map(button => button.dataset.labStage);
  let stage = 'all', focusedStage = stages.find(identifier => identifier !== '0') || stages[0];

  function update() {
    const visibleStages = stage === 'all' ? stages : [stage];
    for (const button of stageButtons) button.setAttribute('aria-pressed', String(button.dataset.labStage === stage));
    for (const button of viewButtons) button.setAttribute('aria-pressed', String(button.dataset.labView === (stage === 'all' ? 'all' : 'stage')));
    matrix.classList.toggle('lab-matrix--focused', stage !== 'all');
    matrix.style.gridTemplateColumns = stage === 'all'
      ? `minmax(116px,.7fr) repeat(${visibleStages.length},minmax(130px,1fr))`
      : 'minmax(140px,190px) minmax(0,1fr)';
    for (const element of matrix.children) {
      const column = visibleStages.indexOf(element.dataset.stage);
      element.hidden = Boolean(element.dataset.stage && column < 0);
      if (element.dataset.stage) element.style.gridColumn = String(column + 2);
    }
    const selected = stage === 'all' ? viewButtons.find(button => button.dataset.labView === 'all') : stageButtons.find(button => button.dataset.labStage === stage);
    const label = selected.querySelector('.lab-step-label') || selected;
    controls.querySelector('.lab-visible-count').textContent = selected.dataset.labCount;
    controls.querySelector('[aria-live]').textContent = `${label.textContent.trim()} · ${selected.dataset.labCount}`;
    if (stage !== 'all') selected.scrollIntoView({block: 'nearest', inline: 'nearest'});
  }

  controls.addEventListener('click', event => {
    const button = event.target.closest('button');
    if (!button) return;
    if (button.hasAttribute('data-lab-reset')) stage = 'all';
    else if (button.dataset.labStage) stage = focusedStage = button.dataset.labStage;
    else if (button.dataset.labView === 'stage') stage = focusedStage;
    update();
  });

  function revealFragment() {
    let identifier;
    try { identifier = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(identifier);
    if (!target || !root.contains(target)) return;
    if (target.closest('.lab-matrix')) {
      stage = 'all'; update();
    }
    target.setAttribute('tabindex', '-1');
    target.focus({preventScroll: true});
    target.scrollIntoView({block: 'start'});
  }
  controls.hidden = false;
  update();
  window.addEventListener('hashchange', revealFragment);
  revealFragment();
})();

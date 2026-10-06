// START_MODULE_CONTRACT
//   PURPOSE: Focus the laboratory matrix without changing its content.
//   SCOPE: Progressive stage/lane selection, reset and fragment visibility.
//   DEPENDS: M-PORTAL-NEIGHBOURS
//   LINKS: M-PORTAL-NEIGHBOURS, V-M-PORTAL-NEIGHBOURS
//   MAP_MODE: SUMMARY
// END_MODULE_CONTRACT
// START_MODULE_MAP
//   update - focus visible matrix coordinates and announce selected groups
//   revealFragment - restore content visibility and focus its linked destination
// END_MODULE_MAP
(() => {
  const root = document.querySelector('.lab-content');
  if (!root) return;
  const matrix = root.querySelector('.lab-matrix');
  const controls = root.querySelector('.lab-controls');
  const stageButtons = [...controls.querySelectorAll('[data-lab-stage]')];
  const laneButtons = [...controls.querySelectorAll('[data-lab-lane]')];
  const stages = stageButtons.slice(1).map(button => button.dataset.labStage);
  const lanes = laneButtons.slice(1).map(button => button.dataset.labLane);
  let stage = 'all', lane = 'all';

  function update() {
    const visibleStages = stage === 'all' ? stages : [stage];
    const visibleLanes = lane === 'all' ? lanes : [lane];
    for (const button of stageButtons) button.setAttribute('aria-pressed', String(button.dataset.labStage === stage));
    for (const button of laneButtons) button.setAttribute('aria-pressed', String(button.dataset.labLane === lane));
    matrix.style.gridTemplateColumns = `minmax(116px,.7fr) repeat(${visibleStages.length},minmax(${visibleStages.length > 3 ? '130px' : '0'},1fr))`;
    for (const element of matrix.children) {
      const column = visibleStages.indexOf(element.dataset.stage);
      const row = visibleLanes.indexOf(element.dataset.lane);
      element.hidden = (element.dataset.stage && column < 0) || (element.dataset.lane && row < 0);
      if (element.dataset.stage) element.style.gridColumn = String(column + 2);
      if (element.dataset.lane) element.style.gridRow = String(row + 2);
    }
    const selected = [...stageButtons, ...laneButtons].filter(button => button.getAttribute('aria-pressed') === 'true');
    controls.querySelector('[aria-live]').textContent = selected.map(button => button.textContent.trim()).join(' · ');
  }

  controls.addEventListener('click', event => {
    const button = event.target.closest('button');
    if (!button) return;
    if (button.hasAttribute('data-lab-reset')) { stage = 'all'; lane = 'all'; }
    else if (button.dataset.labStage) stage = button.dataset.labStage;
    else if (button.dataset.labLane) lane = button.dataset.labLane;
    update();
  });

  function revealFragment() {
    let identifier;
    try { identifier = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(identifier);
    if (!target || !root.contains(target)) return;
    if (target.closest('.lab-matrix')) {
      stage = 'all'; lane = 'all'; update();
    }
    target.setAttribute('tabindex', '-1');
    target.focus({preventScroll: true});
    target.scrollIntoView({block: 'start'});
  }
  controls.hidden = false;
  window.addEventListener('hashchange', revealFragment);
  revealFragment();
})();

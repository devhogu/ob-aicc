const map = document.querySelector('.flow-first .cl-matrix');
if (map) {
  const focusButton = document.getElementById('map-focus');
  focusButton.addEventListener('click', () => {
    const expanded = document.body.classList.toggle('map-focus');
    focusButton.setAttribute('aria-pressed', String(expanded));
    focusButton.textContent = expanded ? 'Show navigation' : 'Expand map';
  });
  const cards = [...map.querySelectorAll('.cl-card')];
  const title = document.getElementById('map-detail-title');
  const description = document.getElementById('map-detail-description');
  const position = document.getElementById('map-detail-position');
  const stageLink = document.getElementById('map-detail-stage');
  const stages = [...map.querySelectorAll('.cl-chev')];
  const lanes = [...map.querySelectorAll('.cl-lane-label')];
  const stageName = new Map(stages.map(el => [el.dataset.step, el.innerText.trim().replace(/\s+/g, ' ')]));
  const laneName = new Map(lanes.map(el => [el.dataset.lane, el.textContent.trim().replace(/\s+/g, ' ')]));

  function selectCard(card) {
    cards.forEach(item => item.setAttribute('aria-pressed', String(item === card)));
    const cell = card.closest('.cl-cell');
    title.textContent = card.querySelector('.cl-name').textContent.trim();
    description.textContent = card.querySelector('.cl-desc').textContent.trim();
    position.textContent = `${stageName.get(cell.dataset.step)} · ${laneName.get(cell.dataset.lane)}`;
    stageLink.href = `#stage-${cell.dataset.step}`;
    stageLink.textContent = `Read ${stageName.get(cell.dataset.step)} notes →`;
  }

  cards.forEach(card => card.addEventListener('click', () => selectCard(card)));
  selectCard(cards[0]);
}

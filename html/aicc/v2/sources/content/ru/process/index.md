---
title: Процесс
summary: Сквозная модель Хаба: четыре уровня, одна карточка и решения в точках контроля.
order: 0
related: process/portfolio, process/program, process/roles, projects
---

Любая работа с AI проходит один путь — от идеи до результата. Хаб показывает три уровня этого пути: [[funnel|воронку]], [[portfolio|портфель]] и [[program|программу]]. Четвёртый, [[team-level|командный уровень]], живёт в Jira. Через все уровни идёт одна [[project-card|карточка проекта]], а решения принимают в точках контроля — на месте или на форуме своего уровня.

## Четыре уровня {#levels}

<div class="levels-illus">
<div class="band"><div><small>Уровень 1</small><strong>Воронка</strong></div><span>Всё, что предложили: идеи и потребности подразделений, каждая на своей карточке.</span><span>Брать ли в проработку — решает менеджер продукта.</span><span class="where"><a href="page:projects/portfolio">Портфель</a>, колонка «Воронка»</span></div>
<div class="band"><div><small>Уровень 2</small><strong>Портфель</strong></div><span>Инициативы и текущая работа по состояниям: проработка, готово к старту, в работе, завершено.</span><span>Старт, вложение, продолжать ли — бизнес-владелец с менеджером продукта; общая картина — форум управления продуктами.</span><span class="where"><a href="page:projects/portfolio">Портфель</a></span></div>
<div class="band"><div><small>Уровень 3</small><strong>Программа</strong></div><span>Capabilities и Features инициатив на одной доске, итерациями.</span><span>Порядок работ и зависимости — форум решений по программе; приёмка Feature — менеджер продукта.</span><span class="where"><a href="page:projects/program">Программа</a></span></div>
<div class="band jira"><div><small>Уровень 4</small><strong>Командный уровень</strong></div><span>Задачи, ошибки и повседневная работа команд.</span><span>Как сделать задачу — решает команда.</span><span class="where">Jira</span></div>
</div>

## Одна карточка от идеи до результата {#card}

Карточка заводится в воронке и живёт до завершения: на ней задача и ожидаемый результат, люди на трёх ролях, условия старта и остановки, текущее состояние, строки Capabilities и Features с ключами Jira и [[decision-log|журнал решений]]. Её ведёт [[project-manager|руководитель проекта]], а Хаб показывает её как есть. Отдельных отчётов нет: всё, что нужно знать о работе, видно на карточке и в сводных видах раздела [Проекты](page:projects).

## Пять правил {#rules}

- **Решения рядом с работой.** Если правило известно заранее, решает названный человек на месте; форум нужен, чтобы увидеть всю картину и разобрать исключения.
- **Работу вытягивают.** Новая работа начинается, когда освободилось место по [[wip-limit|WIP-лимиту]].
- **Условия известны до старта.** [[exit-criterion|Критерий выхода]], [[appetite|допустимый объём вложений]] и [[stop-threshold|порог остановки]] записаны на карточке заранее.
- **Глубина по риску.** Сколько проверять, задаёт [[risk-tier|категория риска]], а не вид работы.
- **Только нужное.** Сохраняются те шаги и записи, которыми кто-то пользуется.

## Как устроен раздел {#map}

<ul class="o-grid card-list cards-compact read-further">
<li class="o-card linked card--compact"><p class="card-kicker">Уровни 1–2</p><h3><a href="page:process/portfolio">Воронка и портфель</a></h3><p class="card-desc">Как принести идею, канбан портфеля, состояния, решения и классы обслуживания.</p></li>
<li class="o-card linked card--compact"><p class="card-kicker">Уровни 3–4</p><h3><a href="page:process/program">Программа</a></h3><p class="card-desc">Доска и бэклог программы, рабочий цикл и связь с Jira.</p></li>
<li class="o-card linked card--compact"><p class="card-kicker">Люди</p><h3><a href="page:process/roles">Роли и форумы</a></h3><p class="card-desc">Три роли, кто что решает, два форума и показатели потока.</p></li>
<li class="o-card linked card--compact"><p class="card-kicker">Виды работы</p><h3><a href="page:process/profiles">Профили проектов</a></h3><p class="card-desc">Как обычно устроены четыре вида работы и что в них принято проверять.</p></li>
</ul>

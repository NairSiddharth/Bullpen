---
layout: page
title: Hall of Fame Tracker
permalink: /hall-of-fame/
use_banner: true
nav: true
nav_order: 2
nav_group: left
description: Track Houston sports Hall of Fame candidates with up-to-date stats, rankings, and player insights.
---

<!-- Retro Hologram Banner -->
<div class="holo-banner about-banner">
  <h1 class="holo-title">Houston Sports Hall of Fame Tracker</h1>
</div>

<section class="halloffameexplanation">
  <p>
    All ACTIVE AND CURRENT (sorry JJ, Harden, Verlander, DHop) Houston sports players (primarily Rockets, Texans, and Astros, with potential inclusion of other sports) currently on track for Hall of Fame induction.
  </p>
</section>

<section class="halloffamecategories">
  <p>Categorized by: INNER-CIRCLE (Among the best at their position, usually marked by MVP-level seasons. Potential for first-ballot), STRONG (meets the requirements for their sports Hall of Fame), BORDERLINE (contentious, flip a coin on candidacy), LONGSHOT (had some good seasons, needs career resurgence or voter partiality), ON-TRACK (if continues on pace, will move into STRONG. 3-5 seasons), PROMISING (early career prospect being highlighted 1-3 seasons).</p>
</section>

<!-- Filter Bar -->
<div class="hof-filter-bar">
  <button data-filter="all" class="active">All</button>
  <button data-filter="inner-circle">Lock</button>
  <button data-filter="strong">Strong</button>
  <button data-filter="borderline">Borderline</button>
  <button data-filter="longshot">Longshot</button>
  <button data-filter="on-track">On Track</button>
  <button data-filter="promising">Promising</button>
</div>

<!-- Card Grid -->
<div class="hof-card-grid">

  <!-- Example Player Card -->
{% for player in site.data.players %}
  {% include player-card.html player=player %}
{% endfor %}
 <!-- Add additional player cards here -->
</div>

<!-- JavaScript for Flip/Expand & Filter -->
<script>
document.querySelectorAll('.player-card').forEach(card => {
  card.addEventListener('click', () => {
    if (!card.classList.contains('state-back') && !card.classList.contains('state-expanded')) {
      card.classList.add('state-back');
    } else if (card.classList.contains('state-back')) {
      card.classList.remove('state-back');
      card.classList.add('state-expanded');
    } else {
      card.classList.remove('state-expanded');
    }
  });
});

document.querySelectorAll('.hof-filter-bar button').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.hof-filter-bar button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const filter = btn.dataset.filter;
    document.querySelectorAll('.player-card').forEach(card => {
      if (filter === "all" || card.dataset.rank === filter) {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  });
});
</script>

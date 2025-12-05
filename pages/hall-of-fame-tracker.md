---
layout: page
title: Hall of Fame Tracker
permalink: /hall-of-fame/
use_banner: true
nav: true
---

<!-- Retro Hologram Banner -->
<div class="holo-banner about-banner">
  <h1 class="holo-title">Houston Sports Hall of Fame Tracker</h1>
</div>

<section class="halloffameexplanation">
  <p>
    All Houston sports players (primarily Rockets, Texans, and Astros, with optional inclusion of other area players)   currently on track for Hall of Fame induction.
  </p>
</section>

<section class="halloffamecategories">
  <p>Categorized by: LOCK, 50-50, DOUBTFUL, ON-TRACK, PROMISING.</p>
</section>

<!-- Filter Bar -->
<div class="hof-filter-bar">
  <button data-filter="all" class="active">All</button>
  <button data-filter="lock">Lock</button>
  <button data-filter="50-50">50/50</button>
  <button data-filter="on-track">On Track</button>
  <button data-filter="promising">Promising</button>
  <button data-filter="doubtful">Doubtful</button>
</div>

<!-- Card Grid -->
<div class="hof-card-grid">

  <!-- Example Player Card -->
{% for player in site.data.players %}
  {% include player-card.html player=player %}
{% endfor %}

</div>

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

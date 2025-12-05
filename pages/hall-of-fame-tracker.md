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
  <h2>
    All Houston sports players (primarily Rockets, Texans, and Astros, with optional inclusion of other area players)   currently on track for Hall of Fame induction.
  </h2>
</section>

<section class="halloffamecategories">
  <h3>Categorized by: LOCK, 50-50, DOUBTFUL, ON-TRACK, PROMISING.</h3>
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
<div class="player-card" data-rank="lock" data-sport="mlb">
  <div class="card-inner">
    <!-- Front -->
    <div class="card-face card-front">
      <!-- Player Photo -->
      <img class="player-photo" src="/assets/images/altuvecard.png" alt="José Altuve">

      <!-- Stats -->
      <div class="card-stats">
        <h2>José Altuve</h2>
        <p>Hits: 2,100+</p>
        <p>HR: 200+</p>
        <p>SB: 300+</p>
        <p>WAR: 60+</p>
      </div>
    </div>

    <!-- Back -->
    <div class="card-face card-back">
      <h3>HOF Pace</h3>
      <p>2B percentile vs HOF: 92%</p>
      <p>Career WAR Pace: Above HOF Average</p>
      <p>Peak WAR: Meets Standard</p>
    </div>

    <!-- Expanded -->
    <div class="card-face card-expanded">
      <h3>Summary</h3>
      <p>
        Altuve is projected as a first-ballot Hall of Famer given elite postseason résumé,
        MVP-caliber peak, and career WAR totals exceeding most HOF second basemen.
      </p>
    </div>
  </div>
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

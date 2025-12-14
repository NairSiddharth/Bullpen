---
layout: page
title: About
permalink: /about/
use_banner: true
nav: true
nav_order: 2
---

<!-- Retro Hologram Banner -->
<div class="holo-banner about-banner">
  <h1 class="holo-title">About Full Count</h1>
</div>

<div class="about-intro">
  <p>
    I'm Sid — a lifelong Houstonian writing about baseball, football, and basketball in the city I grew up in.
    Full Count blends sports commentary with analytical depth, using my software background to create
    simulations, visualizations, and data-backed breakdowns of plays, rosters, trends, and strategy.
  </p>

  <p>
    Whether you follow the Astros, Texans, or Rockets, this site aims to mix fandom with quant thinking,
    exploring both the narratives and the underlying numbers that shape Houston sports.
  </p>

  <p>
    {% include email.html %}
  </p>
</div>

<!-- Neon Team Card Grid -->
<div class="team-card-grid">

  <!-- Astros Card -->
  <div class="team-card neon-card">
    <div class="team-icon">
        <img src="{{ '/assets/icons/baseball.svg' | relative_url }}" alt="Baseball Icon">
    </div>
    <h2 class="team-name">Houston Astros</h2>
    <p>Deep dives into pitching models, hitter streak analysis, Statcast breakdowns, and postseason simulations.</p>
  </div>

  <!-- Rockets Card -->
  <div class="team-card neon-card">
    <div class="team-icon">
        <img src="{{ '/assets/icons/basketball.svg' | relative_url }}" alt="Basketball Icon">
    </div>
    <h2 class="team-name">Houston Rockets</h2>
    <p>Shot selection analytics, lineup efficiency modeling, and game-by-game data visualization.</p>
  </div>

  <!-- Texans Card -->
  <div class="team-card neon-card">
    <div class="team-icon">
        <img src="{{ '/assets/icons/football.svg' | relative_url }}" alt="Football Icon">
    </div>
    <h2 class="team-name">Houston Texans</h2>
    <p>Drive efficiency charts, QB breakdowns, EPA modeling, and defensive coverage exploration.</p>
  </div>

</div>

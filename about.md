---
layout: page
title: About
permalink: /about/
use_banner: true
nav: true
nav_order: 1
nav_group: left
---

<!-- Retro Hologram Banner -->
<div class="holo-banner about-banner">
  <h1 class="holo-title">About Full Count</h1>
</div>

<div class="about-intro">
  <p>
    I'm Sid, a Houston native writing about the Astros, Texans, and Rockets. This sits somewhere between fandom and analysis (I keep my writing as neutral as possible, but I am a fan at the end of the day). I'm not chasing breaking news or game recaps. I'm trying to figure out why something's happening and what it means going forward. If I can better my writing skills while doing so, all the better.
  </p>
  <p>
    Numbers are the name of the game here. I use visualizations, projections, models, and data from all sources alongside longer writing because I want a meaningful answer. Whether it's projecting Altuve's path to 3,000 hits or breaking down how a role change affects team efficiency, the goal is understanding what's happening under the surface.
  </p>
  <p>
    Full Count includes ongoing analytical projects that I found interesting and thought added value for any prospective readers, like you! Take the Hall of Fame tracker, it exists because quantifying careers properly matters more than most casual conversations acknowledge.
  </p>
  <p>
    The writing aims to be readable. Numbers tell stories, but they don't replace them. If you follow Houston sports and want context over headlines, if you're interested in why teams make moves and how player profiles develop over time, this is written for you.
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

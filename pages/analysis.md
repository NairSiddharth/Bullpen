---
layout: page
title: Analysis Index
permalink: /analysis/
use_banner: true
nav: true
---

<div class="analysis-index">

  <!-- Player Development -->
  <section class="analysis-section">
    <h2 class="analysis-title">Player Development</h2>
    <p class="analysis-desc">
      How individual players evolve — skill growth, role changes, and long-term projection.
    </p>

    <div class="post-grid analysis-grid">
      {% assign dev_posts = site.posts | where_exp:"post","post.tags contains 'player-development'" | slice: 0, 4 %}
      {% for post in dev_posts %}
        {% include post_card.html post=post %}
      {% endfor %}
    </div>

    <div class="analysis-cta">
      <a href="{{ '/tags/player-development/' | relative_url }}">View all →</a>
    </div>
  </section>

  <!-- Scheme & Strategy -->
  <section class="analysis-section">
    <h2 class="analysis-title">Scheme & Strategy</h2>
    <p class="analysis-desc">
      Tactical breakdowns, lineup construction, spacing theory, and in-game adjustments.
    </p>

    <div class="post-grid analysis-grid">
      {% assign scheme_posts = site.posts | where_exp:"post","post.tags contains 'scheme'" | slice: 0, 4 %}
      {% for post in scheme_posts %}
        {% include post_card.html post=post %}
      {% endfor %}
    </div>

    <div class="analysis-cta">
      <a href="{{ '/tags/scheme/' | relative_url }}">View all →</a>
    </div>
  </section>

  <!-- Team Analysis -->
  <section class="analysis-section">
    <h2 class="analysis-title">Team Analysis</h2>
    <p class="analysis-desc">
      Comprehensive evaluations of team performance, chemistry, and organizational direction.
    </p>

    <div class="post-grid analysis-grid">
      {% assign team_posts = site.posts | where_exp:"post","post.tags contains 'team'" | slice: 0, 4 %}
      {% for post in team_posts %}
        {% include post_card.html post=post %}
      {% endfor %}
    </div>

    <div class="analysis-cta">
      <a href="{{ '/tags/team/' | relative_url }}">View all →</a>
    </div>
  </section>

</div>

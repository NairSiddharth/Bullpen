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
        <article class="post-card neon-card">

          {% if post.image %}
          <div class="post-card-img-wrapper">
            <img src="{{ post.image | relative_url }}" class="post-card-img" />
          </div>
          {% endif %}

          <h2 class="post-card-title">
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          </h2>

          <div class="post-card-meta">
            {{ post.date | date: "%b %d, %Y" }}
            {% include read_time.html content=post.content %}
          </div>

          <p class="post-card-excerpt">
            {{ post.excerpt }}
          </p>

        </article>
      {% endfor %}
    </div>

    <div class="analysis-cta">
      <a href="{{ '/tags/player-development/' | relative_url }}">View all →</a>
    </div>
  </section>

</div>

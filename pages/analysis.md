---
layout: page
title: Analysis Index
permalink: /analysis/
use_banner: true
nav: true
nav_order: 3
nav_group: right
---

{% assign dev_posts = site.posts | where_exp:"post","post.tags contains 'player-development'" %}
{% assign featured_dev = dev_posts | where: "featured_player", true | first %}

{% assign scheme_posts = site.posts | where_exp:"post","post.tags contains 'scheme'" %}
{% assign featured_scheme = scheme_posts | where: "featured_scheme", true | first %}

{% assign team_posts = site.posts | where_exp:"post","post.tags contains 'team'" %}
{% assign featured_team = team_posts | where: "featured_team", true | first %}

<div class="holo-banner">
  <h1 class="holo-title">Analysis Index</h1>
</div>

<!-- Player Development -->
<section class="analysis-section">
  <h2 class="analysis-title">Player Development</h2>
  <p class="analysis-desc">
    How individual players evolve — skill growth, role changes, and long-term projection.
  </p>

  {% if featured_dev %}
    <article class="post-card neon-card featured-card">
      {% if featured_dev.image %}
        <div class="post-card-img-wrapper">
          <img src="{{ featured_dev.image | relative_url }}" class="post-card-img" />
        </div>
      {% endif %}

      <h3 class="post-card-title">
        <a href="{{ featured_dev.url | relative_url }}">{{ featured_dev.title }}</a>
      </h3>

      <div class="post-card-meta home-meta">
        <span>{{ featured_dev.date | date: "%b %d, %Y" }}</span>
        <span class="separator">|</span>
        <span>{% include read_time.html content=featured_dev.content %}</span>
      </div>

      <p class="post-card-excerpt">{{ featured_dev.excerpt }}</p>
    </article>
  {% endif %}

  <div class="post-grid analysis-grid">
    {% for post in dev_posts %}
      {% unless post == featured_dev %}
        <article class="post-card neon-card">
          {% if post.image %}
            <div class="post-card-img-wrapper">
              <img src="{{ post.image | relative_url }}" class="post-card-img" />
            </div>
          {% endif %}

          <h2 class="post-card-title">
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          </h2>

          <div class="post-card-meta home-meta">
            <span>{{ post.date | date: "%b %d, %Y" }}</span>
            <span class="separator">|</span>
            <span>{% include read_time.html content=post.content %}</span>
          </div>

          <p class="post-card-excerpt">{{ post.excerpt }}</p>
        </article>
      {% endunless %}
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

  {% if featured_scheme %}
    <article class="post-card neon-card featured-card">
      {% if featured_scheme.image %}
        <div class="post-card-img-wrapper">
          <img src="{{ featured_scheme.image | relative_url }}" class="post-card-img" />
        </div>
      {% endif %}

      <h3 class="post-card-title">
        <a href="{{ featured_scheme.url | relative_url }}">{{ featured_scheme.title }}</a>
      </h3>

      <div class="post-card-meta home-meta">
        <span>{{ featured_scheme.date | date: "%b %d, %Y" }}</span>
        <span class="separator">|</span>
        <span>{% include read_time.html content=featured_scheme.content %}</span>
      </div>

      <p class="post-card-excerpt">{{ featured_scheme.excerpt }}</p>
    </article>
  {% endif %}

  <div class="post-grid analysis-grid">
    {% for post in scheme_posts %}
      {% unless post == featured_scheme %}
        <article class="post-card neon-card">
          {% if post.image %}
            <div class="post-card-img-wrapper">
              <img src="{{ post.image | relative_url }}" class="post-card-img" />
            </div>
          {% endif %}

          <h2 class="post-card-title">
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          </h2>

          <div class="post-card-meta home-meta">
            <span>{{ post.date | date: "%b %d, %Y" }}</span>
            <span class="separator">|</span>
            <span>{% include read_time.html content=post.content %}</span>
          </div>

          <p class="post-card-excerpt">{{ post.excerpt }}</p>
        </article>
      {% endunless %}
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

  {% if featured_team %}
    <article class="post-card neon-card featured-card">
      {% if featured_team.image %}
        <div class="post-card-img-wrapper">
          <img src="{{ featured_team.image | relative_url }}" class="post-card-img" />
        </div>
      {% endif %}

      <h3 class="post-card-title">
        <a href="{{ featured_team.url | relative_url }}">{{ featured_team.title }}</a>
      </h3>

      <div class="post-card-meta home-meta">
        <span>{{ featured_team.date | date: "%b %d, %Y" }}</span>
        <span class="separator">|</span>
        <span>{% include read_time.html content=featured_team.content %}</span>
      </div>

      <p class="post-card-excerpt">{{ featured_team.excerpt }}</p>
    </article>
  {% endif %}

  <div class="post-grid analysis-grid">
    {% for post in team_posts %}
      {% unless post == featured_team %}
        <article class="post-card neon-card">
          {% if post.image %}
            <div class="post-card-img-wrapper">
              <img src="{{ post.image | relative_url }}" class="post-card-img" />
            </div>
          {% endif %}

          <h2 class="post-card-title">
            <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          </h2>

          <div class="post-card-meta home-meta">
            <span>{{ post.date | date: "%b %d, %Y" }}</span>
            <span class="separator">|</span>
            <span>{% include read_time.html content=post.content %}</span>
          </div>

          <p class="post-card-excerpt">{{ post.excerpt }}</p>
        </article>
      {% endunless %}
    {% endfor %}
  </div>

  <div class="analysis-cta">
    <a href="{{ '/tags/team/' | relative_url }}">View all →</a>
  </div>
</section>

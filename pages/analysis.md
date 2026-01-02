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

{% assign outlook_posts = site.posts | where_exp:"post","post.tags contains 'outlook'" %}
{% assign featured_outlook = outlook_posts | where: "featured_outlook", true | first %}

{% assign fa_posts = site.posts | where_exp: "post", "post.tags contains 'free-agency'" %}
{% assign trade_posts = site.posts | where_exp: "post", "post.tags contains 'trade'" %}
{% assign move_posts = fa_posts | concat: trade_posts | uniq %}
{% assign featured_move = move_posts | where: "featured_move", true | first %}

{% assign awards_posts = site.posts | where_exp:"post","post.tags contains 'awards'" %}
{% assign featured_awards = awards_posts | where: "featured_awards", true | first %}

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
          <img src="{{ featured_dev.image | relative_url }}" class="post-card-img" alt="{{ featured_dev.title }}"/>
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
              <img src="{{ post.image | relative_url }}" class="post-card-img" alt="{{ post.title }}"/>
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
</section>

<!-- Scheme & Roles -->
<section class="analysis-section">
  <h2 class="analysis-title">Scheme & Roles</h2>
  <p class="analysis-desc">
    Tactical breakdowns, lineup construction, and identifying who does what and why.
  </p>

  {% if featured_scheme %}
    <article class="post-card neon-card featured-card">
      {% if featured_scheme.image %}
        <div class="post-card-img-wrapper">
          <img src="{{ featured_scheme.image | relative_url }}" class="post-card-img" alt="{{ featured_scheme.title }}"/>
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
              <img src="{{ post.image | relative_url }}" class="post-card-img" alt="{{ post.title }}"/>
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
</section>

<!-- Team Outlook -->
<section class="analysis-section">
  <h2 class="analysis-title">Team Outlook</h2>
  <p class="analysis-desc">
    Projections, playoff paths, and evaluating where teams stand as contenders.
  </p>

  {% if featured_outlook %}
    <article class="post-card neon-card featured-card">
      {% if featured_outlook.image %}
        <div class="post-card-img-wrapper">
          <img src="{{ featured_outlook.image | relative_url }}" class="post-card-img" alt="{{ featured_outlook.title }}"/>
        </div>
      {% endif %}

      <h3 class="post-card-title">
        <a href="{{ featured_outlook.url | relative_url }}">{{ featured_outlook.title }}</a>
      </h3>

      <div class="post-card-meta home-meta">
        <span>{{ featured_outlook.date | date: "%b %d, %Y" }}</span>
        <span class="separator">|</span>
        <span>{% include read_time.html content=featured_outlook.content %}</span>
      </div>

      <p class="post-card-excerpt">{{ featured_outlook.excerpt }}</p>
    </article>
  {% endif %}

  <div class="post-grid analysis-grid">
    {% for post in outlook_posts %}
      {% unless post == featured_outlook %}
        <article class="post-card neon-card">
          {% if post.image %}
            <div class="post-card-img-wrapper">
              <img src="{{ post.image | relative_url }}" class="post-card-img" alt="{{ post.title }}"/>
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
</section>

<!-- Trades & Free Agency -->
<section class="analysis-section">
  <h2 class="analysis-title">Trades & Free Agency</h2>
  <p class="analysis-desc">
    Transaction analysis, trade evaluations, and free agent signings.
  </p>

  {% if featured_move %}
    <article class="post-card neon-card featured-card">
      {% if featured_move.image %}
        <div class="post-card-img-wrapper">
          <img src="{{ featured_move.image | relative_url }}" class="post-card-img" alt="{{ featured_move.title }}"/>
        </div>
      {% endif %}

      <h3 class="post-card-title">
        <a href="{{ featured_move.url | relative_url }}">{{ featured_move.title }}</a>
      </h3>

      <div class="post-card-meta home-meta">
        <span>{{ featured_move.date | date: "%b %d, %Y" }}</span>
        <span class="separator">|</span>
        <span>{% include read_time.html content=featured_move.content %}</span>
      </div>

      <p class="post-card-excerpt">{{ featured_move.excerpt }}</p>
    </article>
  {% endif %}

  <div class="post-grid analysis-grid">
    {% for post in move_posts %}
      {% unless post == featured_move %}
        <article class="post-card neon-card">
          {% if post.image %}
            <div class="post-card-img-wrapper">
              <img src="{{ post.image | relative_url }}" class="post-card-img" alt="{{ post.title }}"/>
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
</section>

<!-- Award Watch -->
<section class="analysis-section">
  <h2 class="analysis-title">Award Watch</h2>
  <p class="analysis-desc">
    Tracking MVP races, All-Pro cases, and individual accolades across Houston sports.
  </p>

  {% if featured_awards %}
    <article class="post-card neon-card featured-card">
      {% if featured_awards.image %}
        <div class="post-card-img-wrapper">
          <img src="{{ featured_awards.image | relative_url }}" class="post-card-img" alt="{{ featured_awards.title }}"/>
        </div>
      {% endif %}

      <h3 class="post-card-title">
        <a href="{{ featured_awards.url | relative_url }}">{{ featured_awards.title }}</a>
      </h3>

      <div class="post-card-meta home-meta">
        <span>{{ featured_awards.date | date: "%b %d, %Y" }}</span>
        <span class="separator">|</span>
        <span>{% include read_time.html content=featured_awards.content %}</span>
      </div>

      <p class="post-card-excerpt">{{ featured_awards.excerpt }}</p>
    </article>
  {% endif %}

  <div class="post-grid analysis-grid">
    {% for post in awards_posts %}
      {% unless post == featured_awards %}
        <article class="post-card neon-card">
          {% if post.image %}
            <div class="post-card-img-wrapper">
              <img src="{{ post.image | relative_url }}" class="post-card-img" alt="{{ post.title }}"/>
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
</section>

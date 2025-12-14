---
layout: page
title: Analysis Index
permalink: /analysis/
use_banner: true
nav: true
---

{% assign dev_posts = site.posts | where_exp:"post","post.tags contains 'player-development'" %}
{% assign featured_dev = dev_posts | where: "featured", true | first %}

<div class="analysis-index">

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

        <div class="featured-content">
          <h3 class="post-card-title">
            <a href="{{ featured_dev.url | relative_url }}">
              {{ featured_dev.title }}
            </a>
          </h3>

          <div class="post-card-meta">
            {{ featured_dev.date | date: "%b %d, %Y" }}
            {% include read_time.html content=featured_dev.content %}
          </div>

          <p class="post-card-excerpt">
            {{ featured_dev.excerpt }}
          </p>
        </div>
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

            <div class="post-card-meta">
              {{ post.date | date: "%b %d, %Y" }}
              {% include read_time.html content=post.content %}
            </div>

            <p class="post-card-excerpt">
              {{ post.excerpt }}
            </p>

          </article>
        {% endunless %}
      {% endfor %}
    </div>

    <div class="analysis-cta">
      <a href="{{ '/tags/player-development/' | relative_url }}">View all →</a>
    </div>
  </section>

</div>

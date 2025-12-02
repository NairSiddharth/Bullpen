---
layout: default
title: Tags
permalink: /tags/
---

<h1>Tags</h1>

<ul class="tag-list">
  {% for tag in site.tags %}
    {% assign tag_name = tag[0] %}
    <li>
      <a href="{{ '/tag/' | append: tag_name | append: '/' | relative_url }}">
        {{ tag_name }}
      </a>
      ({{ tag[1].size }})
    </li>
  {% endfor %}
</ul>

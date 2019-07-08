---
layout: archive
title: "Code"
permalink: /code/
author_profile: true
---

{% if author.github %}
  You can also find something here on <u><a href="{{author.github}}">my GitHub</a>.</u>
{% endif %}

{% include base_path %}

## Software

{% for post in site.code reversed %}
  {% if post.type == "software" %}
    {% include archive-item.html %}
  {% endif %}
{% endfor %}

## Experiments

{% for post in site.code reversed %}
  {% if post.type == 'experiment' %}
    {% include archive-item.html %}
  {% endif %}
{% endfor %}

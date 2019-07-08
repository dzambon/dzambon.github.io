---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

## Journal articles
{% for post in site.publications reversed %}
  {% if post.type == "journal" %}
    {% include archive-item.html %}
  {% endif %}
{% endfor %}

## Conferences
{% for post in site.publications reversed %}
  {% if post.type == "conference" %}
    {% include archive-item.html %}
  {% endif %}
{% endfor %}


## Preprints
{% for post in site.publications reversed %}
  {% if post.type == "preprint" %}
    {% include archive-item.html %}
  {% endif %}
{% endfor %}

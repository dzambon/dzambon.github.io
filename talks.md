---
layout: default
title: Daniele's talks
---

## Talks


{% assign talks = site.data.talks.talks | sort: 'date' | reverse %}
{% for talk in talks -%}
- <small>[{{ talk.type }}]</small> <b>{{ talk.venue }}</b>. _{{ talk.title }}_. {{ talk.date | date: "%B %Y" }}, {{ talk.city }}.
  {%- if talk.url -%}&nbsp;<small>[[link]({{ course.ects }})]</small>{%- endif %} 
  {%- if talk.slides -%}&nbsp;<small>[[slides]({{ talk.slides }})]</small>{%- endif %}
  {%- if talk.video -%}&nbsp;<small>[[recording]({{ talk.video }})]</small>{%- endif %} 
  {%- if talk.video -%}&nbsp;<small>[[demo]({{ talk.demo }})]</small>{%- endif %} 
{% endfor %}
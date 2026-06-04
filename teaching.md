---
layout: default
title: Daniele's teaching
---

## Teaching


{% for course in site.data.teaching.courses -%}
{%- assign last_edition = course.editions | last -%}
- [**{{ course.name }}**]({{ last_edition.link }}) {%- if course.level %} ({{ course.level }}){%- endif %}. 
{{ course.role }}.
   - {% for ed in course.editions -%}[{{ ed.year }}]({{ ed.link }})&nbsp;&nbsp;&nbsp;{%- endfor %}  
{% if course.descr %}   - Duties: {{course.descr}}{% endif %}
{% endfor %}


<!-- ## Advised students

{% for student in site.data.students.students -%}
- __{{ student.name }}__, {{student.level}}, {{student.year}}{%- if student.thesis -%}, _{{student.thesis}}_{%- endif -%}. 
{% endfor %}

 -->
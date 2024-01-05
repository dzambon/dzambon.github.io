---
layout: default
title: Daniele's teaching
---

## Teaching


{% for course in site.data.teaching.courses -%}
{%- assign last_edition = course.editions | last -%}
- [**{{ course.name }}**]({{ last_edition.link }}) ({{ course.level }}). 
Director: {{ course.director }}, {% if course.ects -%}ECTS: {{ course.ects }}{%- endif %}.
   - {% for ed in course.editions -%}[{{ ed.year }}]({{ ed.link }})&nbsp;&nbsp;&nbsp;{%- endfor %}  
{% if course.descr %}   - Duties: {{course.descr}}{% endif %}
{% endfor %}


<!-- ## Advised students

{% for student in site.data.students.students -%}
- __{{ student.name }}__, {{student.level}}, {{student.year}}{%- if student.thesis -%}, _{{student.thesis}}_{%- endif -%}. 
{% endfor %}

 -->
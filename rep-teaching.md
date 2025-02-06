---
layout: default
title: Daniele's teaching
---


## Teaching activities

<!-- 
{% for course in site.data.teaching.courses -%}
{%- assign last_edition = course.editions | last -%}
**{{ course.name }}** (ECTS: {{course.ects}})
- Main roles: **{{ course.role }}**.   
- {{ course.level }}, Universita' della Svizzera italiana, Switzerland.
{%- if course.hours %}- Hours: {{course.hours}}{% endif %} 
- Editions: {% for ed in course.editions %}{{ ed.year }}, {% endfor %}    
- Duties: {{course.descr}}.  
- Director: {{ course.director }}. 

{% endfor %} -->


{% for course in site.data.teaching.courses -%}
**{{ course.name }}** (ECTS: {{course.ects}}, Course director: *{{ course.director }}*) 
- {% for lev in course.level_verb %}{{ lev }}, {% endfor %} {{course.institute}}.  
- _Main role_: **{{course.role}}** ({{course.duties}}).  
- _Terms_: {% for ed in course.editions %}{{ ed.year }}, {% endfor %}   
{% if course.workload %}- _Estimated total workload per term_: {{course.workload}}.{% endif %}

{% endfor %}

{% for course in site.data.teaching.courses -%}
\cvline\{..\}\{\textbf\{ {{ course.name }}\} (ECTS: {{course.ects}}, Course director:\textit\{ {{ course.director }}\})  
\begin{itemize}  
\item {% for lev in course.level_verb %}{{ lev }}, {% endfor %} {{course.institute}}.  
\item \textit\{Main role\}:\textbf\{ {{course.role}}\} ({{course.duties}}).  
{% if course.workload %}\{\small \textit\{Estimated total workload per term\}: {{course.workload}}.\}{% endif %}  
\item \textit\{Terms\}: {% for ed in course.editions %}{{ ed.year }}, {% endfor %}   
\end{itemize}\}   
%   
{% endfor %}

---

## Tutorials

<!-- 
{% for course in site.data.teaching.courses -%}
{%- assign last_edition = course.editions | last -%}
**{{ course.name }}** (ECTS: {{course.ects}})
- Main roles: **{{ course.role }}**.   
- {{ course.level }}, Universita' della Svizzera italiana, Switzerland.
{%- if course.hours %}- Hours: {{course.hours}}{% endif %} 
- Editions: {% for ed in course.editions %}{{ ed.year }}, {% endfor %}    
- Duties: {{course.descr}}.  
- Director: {{ course.director }}. 

{% endfor %} -->


{% for course in site.data.teaching.tutorial -%}
**{{ course.name }}** (Duration: {{course.duration}})
- {{course.institute}}
- [{{course.link}}]({{course.link}}) 
{% if course.duties %}- {{course.duties}}.{% endif %}

{% endfor %}

---

## Student supervision and tutoring

{% for student in site.data.students.students -%}
__{{ student.name }}__ ({{student.year}}, {{student.role}})   
- {{student.level_verb}}, {{student.institute}}.  
{% if student.thesis %}- Thesis: _{{student.thesis}}_.{% endif %}

{% endfor %}

{% for student in site.data.students.students -%}   
\cvline\{ {{student.year}}\}\{\textbf\{ {{ student.name }}\} ({{student.role}})   
\begin{itemize}  
\item {{student.level_verb}}, {{student.institute}}.    
{% if student.thesis %}\item  Thesis:\textit\{ {{student.thesis}}\}.{% endif %}  
\end{itemize}\}     
%   
{% endfor %}   

{% for news in site.data.news -%}
{% if include.type and include.type != news.type -%}
{% else -%}
* <span style="color:#BBB; font-size:small">[{{ news.date }}]</span> {{ news.msg }}
{% endif -%}
{% endfor %}


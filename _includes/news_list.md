{% for news in site.data.news -%}
* <span style="color:#BBB; font-size:small">[{{ news.date }}]</span> {{ news.msg }}
{% endfor %}


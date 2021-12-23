---
layout: default
title: Home
---

<h1 class="landing-title">{{ site.author.name }}</h1>
<div class="profile">
  <img src="{{ site.baseurl }}/images/zambon_d.jpg" class="profile-pic"/>
  <p class="message profile-card">
    Hey there, I am a post-doc at the Swiss AI Lab <a href="https://idsia.ch">IDSIA</a> (CH) in the <a href="https://gmlg.ch">graph machine learning group</a> working with Prof. <a href="http://home.deib.polimi.it/alippi/">Cesare Alippi</a>.
<br/><br/>
    Research interests: graph representation learning, learning in non-stationary environments, and statistical tests for anomaly and change detection.
<br/><br/>
<a href="mailto:firstname.surname@usi.ch">firstname.surname@usi.ch</a>
&nbsp;&middot;&nbsp;
<a href="{{ site.author.github }}"><i class="fa fa-github"></i> GitHub</a>
&nbsp;&middot;&nbsp;
<a href="{{ site.author.google_scholar }}"><i class="ai ai-google-scholar"></i> Google Scholar</a>
&nbsp;&middot;&nbsp;
<a href="{{ site.author.orcid }}"><i class="ai ai-orcid"></i> ORCID</a>
  </p>
</div>



## About me


I obtained my Ph.D. <i class="fa fa-graduation-cap"></i> at the Swiss AI Lab [IDSIA](https://idsia.ch) in the [graph machine learning group](https://gmlg.ch), [USI](http://inf.usi.ch) (CH).
My advisors were Prof. [Cesare Alippi](https://alippi.faculty.polimi.it/) (from [USI](http://inf.usi.ch) and [POLIMI](https://www.deib.polimi.it/eng/home-page)) and Prof. [Lorenzo Livi](https://sites.google.com/site/lorenzlivi/) (from [Univ. of Manitoba](https://sci.umanitoba.ca/cs/), CA, and [Univ. of Exeter](http://emps.exeter.ac.uk/), UK).
My research dealt with statistical tests for anomaly and change detection in sequences of graphs, graph representation learning, and learning in non-stationary environments. You can find a list of my [publications here](#publications).

I have been visiting researcher at the [University of Florida](http://www.cnel.ufl.edu/) (US) working on kernel adaptive methods and the [University of Exeter](http://emps.exeter.ac.uk/) (UK) exploring embeddings onto Riemannian manifolds. I have also been intern at [STMicroelectronics](https://www.st.com) (Italy) where I developed my Master's thesis on sparse models for anomaly detection. 
I received Master's and Bachelor's degrees from the [Università degli Studi di Milano](http://www.matematica.unimi.it/ecm/home) (Italy) focusing on approximation theory and mathematical statistics.

I am (or have been) in the program committee of top-tier conferences and journals of the field, including IEEE TNNLS, IEEE TSP, IEEE PAMI, IEEE IJCNN, NeurIPS, ICLR, ICML, CVPR.


## Publications

{% for paper in site.data.papers -%}
- <a id="{{ paper.id }}" href="">{{paper.title}}</a>, {% if paper.short_venue %}{{paper.short_venue}},{% endif %} {{paper.year}}, <small>{{paper.short_author | replace: "Zambon", "<b>Zambon</b>" }}</small>.    
<span style="top-margin:-5px; margin-left:30px; padding-bottom:125px"> 
{%- if paper.doi %}[<a class="square-button" href="https://doi.org/{{paper.doi}}">DOI</a>]&nbsp;{% endif %}
{%- if paper.url %}[<a class="square-button" href="{{paper.url}}">{{paper.url}}</a>]&nbsp;{% endif %}
{%- if paper.arxiv_id %}[<a class="square-button" href="https://arxiv.org/abs/{{paper.arxiv_id}}">arXiv</a>]&nbsp;{% endif %}
{%- if paper.openreview_id %}[<a class="square-button" href="https://openreview.net/forum?id={{paper.openreview_id}}">OpenReview</a>]&nbsp;{% endif %}
{%- if paper.github %}[<a class="square-button" href="{{paper.github}}"><i class="fa fa-github"></i> GitHub</a>]&nbsp;{% endif %}
{%- if paper.gitlab %}[<a class="square-button" href="{{paper.gitlab}}"><i class="fa fa-gitlab"></i> GitLab</a>]&nbsp;{% endif %}
{%- if paper.experiments %}[<a class="square-button" href="{{paper.experiments}}">experiments</a>]&nbsp;{% endif %}
{%- if paper.bibtex %}[<a class="square-button" href="{{ site.baseurl }}/publications/{{ paper.id }}/#{{paper.bibtex}}">bibtex</a>]{% endif %}
</span>   
{% endfor %}



## Teaching 

I regularly serve a teaching assistant for Master and Bachelor courses at USI helding lectures, lab sessions and examinations.   


{% for course in site.data.teaching.courses -%}
- [{{course.name}}]({{course.link}}) ({{course.year}}, {{course.director}}).
{% endfor %}


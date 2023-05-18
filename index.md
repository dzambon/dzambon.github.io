---
layout: default
title: Home
---

<h1 class="landing-title">{{ site.author.name }}</h1>
<div class="profile-container">
  <img src="{{ site.baseurl }}/images/zambon_d.jpg" class="profile-floated"/>
  <p class="profile-text">
    I am a post-doc at the Swiss AI Lab <a href="https://idsia.ch">IDSIA</a> and <a href="https://usi.ch">USI</a> (CH) in the <a href="https://gmlg.ch">graph machine learning group</a>.
  </p>
  <p class="profile-text">
    The focus of my research is graph representation learning, learning in non-stationary environments, and graph stream processing.
  </p>
  <p class="profile-text">
<a href="mailto:firstname.surname@usi.ch"><i class="fa fa-envelope"></i> firstname.surname@usi.ch</a>
<br/>
<a href="{{ site.author.github }}"><i class="fa fa-github"></i> GitHub</a>
&nbsp;&middot;&nbsp;
<a href="{{ site.author.google_scholar }}"><i class="ai ai-google-scholar"></i> Google Scholar</a>
&nbsp;&middot;&nbsp;
<a href="{{ site.author.linkedin }}"><i class="fa fa-linkedin"></i> LinkedIn</a>
&nbsp;&middot;&nbsp;
<a href="{{ site.author.orcid }}"><i class="ai ai-orcid"></i> ORCID</a>
  </p>
  <div class="profile-clear"></div>
</div>

## News!

* A bunch of preprints on arXiv about: Kalman filters [[1](#alippi2023graph)], spatio-temporal models [[2](#zambon2023graph), [3](#cini2022sparse), [4](#cini2023taming)], and model optimality [[5](#zambon2023where)].
* Our special sessions on [DL4G @ IEEE IJCNN 2023](https://2023.ijcnn.org/paper-submission/special-sessions#session-4-37) and [GRL @ ESANN 2023](https://www.esann.org/special-sessions#session4) will be held soon in Gold Coast (Queensland, AU) and Bruges (BE).
* Paper accepted @ NeurIPS '22. [AZ-whiteness test](#zambon2022aztest): with it you can test the optimality of GNN's.
* We got funded by [OCRE](https://www.ocre-project.eu/news-insights/news/ocre-awards-cloud-adoption-funding-15-exciting-research-projects?utm_source=linkedin.com&utm_medium=social&utm_campaign=15-projects-funded) with cloud computing resources for a project in collaboration with [UniPD](https://www.unipd.it/).


## About me


I obtained my Ph.D. <i class="fa fa-graduation-cap"></i> from [USI Università della Svizzera italiana](http://inf.usi.ch) (CH) under the supervision of Prof. [Cesare Alippi](https://alippi.faculty.polimi.it/) (from [USI](http://inf.usi.ch) and [POLIMI](https://www.deib.polimi.it/eng/home-page)) and Prof. [Lorenzo Livi](https://sites.google.com/site/lorenzlivi/) (from [Univ. of Manitoba](https://sci.umanitoba.ca/cs/), CA, and [Univ. of Exeter](http://emps.exeter.ac.uk/), UK).
My research dealt with statistical tests for anomaly and change detection in sequences of graphs, graph representation learning, and learning in non-stationary environments. You can find a list of my [publications here](#publications).

I have been visiting researcher at the [University of Florida](http://www.cnel.ufl.edu/) (US) working on kernel adaptive methods and at the [University of Exeter](http://emps.exeter.ac.uk/) (UK) exploring embeddings onto Riemannian manifolds. I have also been an intern at [STMicroelectronics](https://www.st.com) (Italy) where I developed my Master's thesis on sparse models for anomaly detection. 
I received Master's and Bachelor's degrees from the [Università degli Studi di Milano](http://www.matematica.unimi.it/ecm/home) (Italy) focusing on approximation theory and mathematical statistics.

I am (or have been) in the program committee of top-tier conferences and journals of the field, including IEEE TNNLS, IEEE TSP, IEEE PAMI, IEEE IJCNN, NeurIPS, ICLR, ICML, CVPR.


## Publications

### Preprints

{% include paper_list.html type="preprint" %}

### Journals

{% include paper_list.html type="journal" %}

### Conferences

{% include paper_list.html type="conference" %}

### Thesis

{% include paper_list.html type="thesis" %}



## Teaching 

I regularly serve as a teacher in Master's and Bachelor's degree programs at USI holding lectures, lab sessions, and examinations.   

{% for course in site.data.teaching.courses -%}
- [{{ course.name }}]({{ course.link }}) ({{ course.year }}). 
{% endfor %}


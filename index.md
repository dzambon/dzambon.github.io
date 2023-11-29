---
layout: default
title: Home
---

<h1 class="landing-title">{{ site.author.name }}</h1>
<div class="profile-container">
  <img src="{{ site.baseurl }}/images/zambon_d.jpg" class="profile-floated"/>
  <p class="profile-text">
    Hello! My name is Daniele, I am a post-doc at the Swiss AI Lab <a href="https://idsia.ch">IDSIA</a>, <a href="https://usi.ch">USI</a>, in the <a href="https://gmlg.ch">Graph Machine Learning Group</a>, and member of the <a href="https://www.learning4graphs.org">IEEE Task Force on Learning for Graphs</a>.
  </p>
  <p class="profile-text">
    The focus of my research is graph representation learning, learning in non-stationary environments, and graph stream processing.
  </p>
  <p class="profile-text">
    <a href="mailto:name.surname@usi.ch"><i class="fa-solid fa-envelope"></i> name.surname@usi.ch</a>
  <br/>
    <a href="https://twitter.com/{{ site.author.twitter }}"><i class="fa-brands fa-x-twitter"></i> Twitter</a>
    &nbsp;&middot;&nbsp;
    <a href="https://www.linkedin.com/in/{{ site.author.linkedin }}"><i class="fa-brands fa-linkedin-in"></i> LinkedIn</a>
    &nbsp;&middot;&nbsp;
    <a href="https://github.com/{{ site.author.github }}"><i class="fa-brands fa-github"></i> GitHub</a>
    &nbsp;&middot;&nbsp;
    <a href="https://scholar.google.ch/citations?user={{ site.author.google_scholar }}"><i class="fa-brands fa-google-scholar"></i> Google Scholar</a>
    &nbsp;&middot;&nbsp;
    <a href="https://orcid.org/{{ site.author.orcid }}"><i class="fa-brands fa-orcid"></i> ORCID</a>
  </p>
  <div class="profile-clear"></div>
</div>


## News!

{% include news_list.md %}


## About me


I obtained my Ph.D. <i class="fa-solid fa-graduation-cap"></i> from [USI](http://inf.usi.ch) <span class="fi fi-ch"></span> (CH) in 2022.
My research dealt with statistical tests for anomaly and change detection, graph representation learning, and learning in non-stationary environments. You can find a list of my [publications here](#publications).

I have been visiting researcher at the [University of Florida](http://www.cnel.ufl.edu/) <span class="fi fi-us"></span> (US, Nov '19--Feb '20) working on kernel adaptive methods and at the [University of Exeter](http://emps.exeter.ac.uk/) <span class="fi fi-gb"></span> (UK, Sep '17, Oct '18) exploring embeddings onto Riemannian manifolds. I have also been an intern at [STMicroelectronics](https://www.st.com) <span class="fi fi-it"></span> (IT, May '15--Apr '16, May '16--Sep '16) where I developed my Master's thesis on sparse models for anomaly detection and co-authored a pantent. 
I received Master's and Bachelor's degrees in mathematics from the [Università degli Studi di Milano](http://www.matematica.unimi.it/ecm/home) <span class="fi fi-it"></span> (IT) focusing on approximation theory and mathematical statistics.

I have published in and have been reviewer for top-tier journals and conferences of the field, including JMLR, IEEE TPAMI, IEEE TNNLS, IEEE TSP, NeurIPS, ICLR, and ICML; I was certified Outstanding Reviewer of 2022 by the IEEE Computational Intelligence society and Top 33% Reviewer for ICML 2020. I hold a patent. I have organized special sessions and tutorials at international conferences on graph deep learning. 

## Publications

### Preprints

{% include paper_list.html type="preprint" %}

### Journals

{% include paper_list.html type="journal" %}

### Conferences

{% include paper_list.html type="conference" %}

### Patents

{% include paper_list.html type="patent" %}

### Thesis

{% include paper_list.html type="thesis" %}

<small>(\* equal contribution.)</small>


## Teaching 

I regularly serve as a teacher in Master's and Bachelor's degree programs at USI holding lectures, lab sessions, and examinations.   

{% for course in site.data.teaching.courses -%}
- [{{ course.name }}]({{ course.link }}) ({{ course.year }}). 
{% endfor %}


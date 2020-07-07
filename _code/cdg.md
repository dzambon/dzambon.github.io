---
title: 'CDG: Change Detection in a sequence of Graphs.'
permalink: /code/cdg
collection: code
type: 'software'
desc: 'This is the reference code for most of my publications.'
experiment: false
github: 'https://github.com/dzambon/cdg.git'
thumbnail: "/images/cdg_logo.svg"
---

{% include base_path %}


### Tutorial

Please have a look at this notebook [`tutorial.ipynb`](https://github.com/dzambon/cdg/blob/master/tutorial.ipynb).

Here a snippet of code to perform a change-detection test on a sequence `x`:
```python
from cdg.changedetection import GaussianCusum
cdt = GaussianCusum()
cdt.fit(x[:N_train])
y = cdt.predict(x[N_train:])
```


### The package

The code is written in `python3`. 
In the package you will find following folders
* **`cdg/graph`** interface for datasets of graphs and dissimilarities.
* **`cdg/embedding`** several types of numeric representations of graphs, such as, dissimilarity representation and manifold embeddings, like [[3]({{ base_path }}/publications/zambon2018anomaly)]. 
* **`cdg/changedetection`** tests for change detection, like [[1]({{ base_path }}/publications/zambon2018concept), [2]({{ base_path }}/publications/zambon2019change)].
* **`cdg/utils`** utilities for the module.
* **`cdg/simulation`** utilities for repeated experiments.



### Installation

Go to your preferred directory, then 
```bash
git clone https://github.com/dzambon/cdg
cd cdg
pip install -e .
```


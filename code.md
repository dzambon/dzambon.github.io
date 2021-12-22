---
layout: page
title: Code and Software
---





## Graph Random Neural Features

Graph Random Neural Features (GRNF) is an embedding method from graph-structured data to real vectors based on a family of graph neural networks. 
GRNF can be used within traditional processing methods or as a training-free input layer of a graph neural network. 
The theoretical guarantees that accompany GRNF ensure that the considered graph distance is metric, hence allowing to distinguish any pair of non-isomorphic graphs, and that GRNF approximately preserves its metric structure. 

Please, refer to these papers for more details: [zambon2020graph]({{ base_path }}/#zambon2020graph), [zambon2019graph]({{ base_path }}/#zambon2019graph).


The [<i class="fa fa-github"></i> GitHub repository](https://github.com/dzambon/graph-random-neural-features.git) provides a [Spektral](graphneural.network) (TensorFlow) implementation:

```python
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from grnf.tf import GraphRandomNeuralFeatures
X_in = Input(shape=(N, F))
A_in = Input(shape=(N, N))
psi = GraphRandomNeuralFeatures(64, activation="relu")([X_in, A_in])
output = Dense(1)(psi)
model = Model(inputs=[X_in, A_in], outputs=output)
```

and a [PyTorch Geometric](https://github.com/rusty1s/pytorch_geometric) one:
```python
from grnf.torch import GraphRandomNeuralFeatures
grnf = GraphRandomNeuralFeatures(64)
z = grnf(data)
```






## CDG: Change Detection in a sequence of Graphs.

This is the reference code for most of my publications. It is an integrated collection of tools for performing change detection.
For further details please visit the [<i class="fa fa-github"></i> GitHub repository](https://github.com/dzambon/cdg).

#### Package

The code is written in `python3`. 
In the package you will find following folders
* **`cdg/graph`** interface for datasets of graphs, distances and kernels.
* **`cdg/embedding`** several types of vector and manifold representations of graphs, such as, dissimilarity representation and manifold embeddings, like [[zambon2018anomaly]({{ base_path }}/#zambon2018anomaly)]. 
* **`cdg/changedetection`** tests for change detection, like [[zambon2018concept]({{ base_path }}/#zambon2018concept), [zambon2019change]({{ base_path }}/#zambon2019change)].
* **`cdg/utils`** utilities for the module.
* **`cdg/simulation`** utilities for running repeated experiments.


#### Tutorial

I have set up a notebook on GitHub for you: [`tutorial.ipynb`](https://github.com/dzambon/cdg/blob/master/tutorial.ipynb).
Here a snippet of code to perform a change-detection test on a sequence `x`:
```python
from cdg.changedetection import GaussianCusum
cdt = GaussianCusum()
cdt.fit(x[:N_train])
y = cdt.predict(x[N_train:])
```






## CPM for graph sequences

Code replicating the experiments of paper [zambon2019change]({{ base_path }}/#zambon2019change).
The code, availabel on [<i class="fa fa-github"></i> GitHub](https://github.com/dzambon/cpm-graph-sequence.git).

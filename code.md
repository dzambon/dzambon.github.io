---
layout: page
title: Code and Software
---


## AZ-whiteness test

<ul id="code-element-list">
	<li><a href="{{ base_path }}/#zambon2022aztest"><i class="fa fa-file"></i> paper</a></li>
	<li><a href="https://github.com/dzambon/az-whiteness-test"><i class="fa fa-github"></i> repository</a></li>
</ul> 

The following example shows how to perform the test in python

```python
from graph_sign_test import az_whiteness_test

# Compute residuals
y_true, edge_index = dataset(...)
model.load(...)
y_pred = model.predict(...)
residuals = y_true - y_pred 
# N, T, F, E = 30, 100, 1, 70
# residuals = np.random.randn(T, N, F)
# edge_index = np.random.randint(N, size=(2, E))

# Perform the AZ-whiteness test
az_test = az_whiteness_test(x=residuals, edge_index=edge_index)
x = signal_gen_fun()
aztest = az_whiteness_test(
	x=residuals, 
	edge_index_spatial=edge_index, 
	edge_weight_temporal="auto", 
	multivariate=True
) # -> AZWhitenessTestResult(statistic=0.251, pvalue=0.801)
```

## Graph Random Neural Features

<ul id="code-element-list">
	<li><a href="{{ base_path }}/#zambon2020graph"><i class="fa fa-file"></i> paper</a></li>
	<li><a href="https://github.com/dzambon/graph-random-neural-features."><i class="fa fa-github"></i> repository</a></li>
</ul> 

A graph-level embedding method based on a family of graph neural networks. 
GRNF can be used within traditional processing methods or as a training-free input layer of a graph neural network. The repository provides a [Spektral](graphneural.network) (TensorFlow) implementation:

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
as well as a [PyTorch Geometric](https://github.com/rusty1s/pytorch_geometric) one:
```python
from grnf.torch import GraphRandomNeuralFeatures
grnf = GraphRandomNeuralFeatures(64)
z = grnf(data)
```




## CDG: Change Detection in a sequence of Graphs.

<ul id="code-element-list">
	<li><a href="https://github.com/dzambon/cdg"><i class="fa fa-github"></i> repository</a></li>
</ul> 

A collection of tools for performing change detection developed during my [PhD]({{ base_path }}/#zambon2022phdthesis).

In the package you will find following folders:
* **`cdg/graph`** interface for datasets of graphs, distances and kernels.
* **`cdg/embedding`** several types of vector and manifold representations of graphs, such as, dissimilarity representation and manifold embeddings, like [[zambon2018anomaly]({{ base_path }}/#zambon2018anomaly)]. 
* **`cdg/changedetection`** tests for change detection, like [[zambon2018concept]({{ base_path }}/#zambon2018concept), [zambon2019change]({{ base_path }}/#zambon2019change)].
* **`cdg/utils`** utilities for the module.
* **`cdg/simulation`** utilities for running repeated experiments.


I have set up a [tutorial notebook](https://github.com/dzambon/cdg/blob/master/tutorial.ipynb) on the GitHub repository;
here a snippet of code to perform a change-detection test on a sequence `x`:
```python
from cdg.changedetection import GaussianCusum
cdt = GaussianCusum()
cdt.fit(x[:N_train])
y = cdt.predict(x[N_train:])
```


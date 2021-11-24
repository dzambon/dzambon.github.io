---
title: 'GRNF: Graph Random Neural Features.'
permalink: /code/grnf
collection: code
type: 'software'
desc: 'Graph Random Neural Features proposed in [Zambon et al. 2020]({{ base_path }}/publications/zambon2020graph).'
github: 'https://github.com/dzambon/graph-random-neural-features.git'
---

{% include base_path %}


Graph Random Neural Features (GRNF) is an embedding method from graph-structured data to real vectors based on a family of graph neural networks. 
GRNF can be used within traditional processing methods or as a training-free input layer of a graph neural network. 
The theoretical guarantees that accompany GRNF ensure that the considered graph distance is metric, hence allowing to distinguish any pair of non-isomorphic graphs, and that GRNF approximately preserves its metric structure. 

Please, refer to these papers for more details: [Zambon et al. 2020]({{ base_path }}/publications/zambon2020graph), [Zambon et al. 2019]({{ base_path }}/publications/zambon2019graph).


The repository [graph-random-neural-features](https://github.com/dzambon/graph-random-neural-features.git) provides a [Spektral](graphneural.network) (TensorFlow) implementation:

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
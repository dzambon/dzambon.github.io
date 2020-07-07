---
collection: code
type: experiment
permalink: /code/zambon2020graph

label: zambon2020graph

experiment: false
github: https://github.com/dzambon/graph-random-neural-features.git
---

The repository [graph-random-neural-features](https://github.com/dzambon/graph-random-neural-features.git) provides a [Spektral](graphneural.network) (TensorFlow) and a [PyTorch Geometric](https://github.com/rusty1s/pytorch_geometric) implementations of Graph Random Neural Features presented in [Zambon et al. 2020]({{ base_path }}/publications/zambon2020graph) and [Zambon et al. 2019]({{ base_path }}/publications/zambon2019graph).

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

```python
from grnf.torch import GraphRandomNeuralFeatures
grnf = GraphRandomNeuralFeatures(64)
z = grnf(data)
```

Experiments are in branch `v0.1.0`.
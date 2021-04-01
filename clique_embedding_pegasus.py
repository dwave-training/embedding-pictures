# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
from random import random

import matplotlib
import networkx as nx
import dwave_networkx as dnx
from minorminer.busclique import find_clique_embedding
from dwave.system.samplers import DWaveSampler

try:
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib.use("agg")
    import matplotlib.pyplot as plt

N = int(sys.argv[1])
G = nx.complete_graph(N)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

node_color_list = [(random(), random(), random()) for i in range(N)]
chain_color_list = {i: node_color_list[i] for i in range(N)}

# Draw the QUBO as a networkx graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, font_size=10, node_size=300, node_color=node_color_list, edge_color='gray', ax=axes[0])

# Draw the embedded graph
dwave_sampler = DWaveSampler(solver={'topology__type__eq': 'pegasus'})
A = dwave_sampler.edgelist
pegasus_graph = dnx.pegasus_graph(16, edge_list=A)
clique_embedding = find_clique_embedding(N, pegasus_graph)

qubits = 0
for chain in clique_embedding.values():
    qubits += len(chain)

print("\nEmbedding for", N, "clique found using", qubits, "qubits.")

dnx.draw_pegasus_embedding(pegasus_graph, clique_embedding, embedded_graph=G, chain_color=chain_color_list, unused_color=None, ax=axes[1])
plt.savefig('clique_embedding_pegasus')

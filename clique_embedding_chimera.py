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

from minorminer import find_embedding
from dwave.system.samplers import DWaveSampler
import matplotlib.pyplot as plt
import networkx as nx
import dwave_networkx as dnx

G = nx.complete_graph(8)

# Do the embedding
dwave_sampler = DWaveSampler(solver={'topology__type__eq': 'chimera'})
A = dwave_sampler.edgelist
embedding = find_embedding(G, A)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

# Draw the QUBO as a networkx graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, font_size=10, node_size=100, node_color='cyan', ax=axes[0])

# Draw the embedded graph
chimera_graph = dnx.chimera_graph(16, 16, 4)
dnx.draw_chimera_embedding(chimera_graph, embedding, embedded_graph=G, unused_color=None, ax=axes[1])
plt.show()

from minorminer.busclique import find_clique_embedding
from dwave.system.samplers import DWaveSampler
import matplotlib.pyplot as plt
import networkx as nx
import dwave_networkx as dnx
import sys
N = int(sys.argv[1])
G = nx.complete_graph(N)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

# Draw the QUBO as a networkx graph
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos=pos, font_size=10, node_size=100, node_color='cyan', ax=axes[0])

# Draw the embedded graph
dwave_sampler = DWaveSampler(solver={'topology__type__eq': 'chimera'})
A = dwave_sampler.edgelist
chimera_graph = dnx.chimera_graph(16, edge_list=A)
clique_embedding = find_clique_embedding(8, chimera_graph)
dnx.draw_chimera_embedding(chimera_graph, clique_embedding, embedded_graph=G, unused_color=None, ax=axes[1])
plt.show()

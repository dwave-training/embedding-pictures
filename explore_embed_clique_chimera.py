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
import networkx as nx
import sys

N = int(sys.argv[1])
G = nx.complete_graph(N)

# Do the embedding
dwave_sampler = DWaveSampler(solver={'topology__type__eq': 'chimera'})
A = dwave_sampler.edgelist
embedding = find_embedding(G, A)
print(embedding)

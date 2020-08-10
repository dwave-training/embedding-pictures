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

import dimod
from minorminer import find_embedding
from dwave.system.samplers import DWaveSampler
from pyqubo import Array
import sys

# Graph partitioning as full mesh
gamma = 3
N = int(sys.argv[1])

# Set up variables
x = Array.create('x', shape=N, vartype='BINARY')

H = gamma * (sum(x) - (N/2)) ** 2
for i in range(N):
    for j in range(i + 1, N):
        H += (x[i] - x[j]) ** 2

# Compile the model, and turn it into a QUBO object
model = H.compile()
Q, offset = model.to_qubo()

# Do the embedding
dwave_sampler = DWaveSampler(solver={'topology__type__eq': 'chimera'})
A = dwave_sampler.edgelist
embedding = find_embedding(Q, A)
print(embedding)

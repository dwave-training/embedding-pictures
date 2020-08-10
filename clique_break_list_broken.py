from minorminer import find_embedding
from dwave.system.samplers import DWaveSampler
from dimod import BinaryQuadraticModel
from dwave.embedding import embed_bqm, broken_chains, unembed_sampleset
import numpy as np
from pyqubo import Array
import sys
import dimod

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
bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=offset)

# Very weak chainstrength in order to show broken chains
chainstrength = 1.01
numruns = 100

dwave_sampler = DWaveSampler(solver={'topology__type__eq': 'chimera'})
A = dwave_sampler.edgelist
Adj = dwave_sampler.adjacency
embedding = find_embedding(Q, A)
print(embedding)

# Cannot use a Composite to get the broken chains, so do the embedding
# directly
bqm_embedded = embed_bqm(bqm, embedding, Adj, chain_strength=chainstrength)
response = DWaveSampler().sample(bqm_embedded, num_reads=numruns)

# We need to get the chains directly, as a list
chains = [embedding[v] for v in bqm.variables]

# Obtain the broken chains
broken = broken_chains(response, chains)

# Interpret the results in terms of the embedding. Be sure to
# tell the method to compute the chain_break_frequency.
print(unembed_sampleset(response, embedding, source_bqm=bqm, chain_break_fraction=True), broken)

# Use NumPy method to obtain the indices of the broken chains
w = np.where(broken)
indices = list(zip(*w))
print(indices)

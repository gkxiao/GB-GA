from rdkit import Chem
import numpy as np
import time
import crossover as co
import scoring_functions as sc
import GB_GA as ga 

n_tries = 1
population_size = 20 
mating_pool_size = 20
generations = 20
mutation_rate = 0.01
co.average_size = 39.15
co.size_stdev = 3.50
scoring_function = sc.logP_score
scoring_args = []

file_name = 'ZINC_first_1000.smi'

print('population_size', population_size)
print('mating_pool_size', mating_pool_size)
print('generations', generations)
print('mutation_rate', mutation_rate)
print('average_size/size_stdev', co.average_size, co.size_stdev)
print('initial pool', file_name)
print('number of tries', n_tries)
print('')

results = []
size = []
t0 = time.time()
all_scores = []
for i in range(n_tries):     
    scores, population = ga.GA(population_size, file_name,scoring_function,generations,mating_pool_size, 
                               mutation_rate,scoring_args)
    all_scores.append(scores)
    print(i, scores[0], Chem.MolToSmiles(population[0]))
    results.append(scores[0])
    #size.append(Chem.MolFromSmiles(sc.max_score[1]).GetNumAtoms())

t1 = time.time()
print('')
print('time ',t1-t0)
print(max(results),np.array(results).mean(),np.array(results).std())
#print(max(size),np.array(size).mean(),np.array(size).std())

#print(all_scores)
# Import comb (combination operation) from the scipy library 
from scipy.special import comb

def calculateProbability(k, m, n):
    # Calculate total number of organisms in the population:
    totalPop = k + m + n 
    # Calculate the number of combos that could be made (valid or not):
    totalCombos = comb(totalPop, 2)
    # Calculate the number of combos that have a dominant allele therefore are valid:
    validCombos = comb(k, 2) + k*m + k*n + .5*m*n + .75*comb(m, 2)
    probability = validCombos/totalCombos
 
    return probability

# Example Call: 
print(calculateProbability(16,30,15))
# Example Output: 0.783333333333



 # total population
hom=16
rec=15
het=30
pop_total = 4 * comb(hom + het + rec, 2)

    # use PUNNETT squares!

    # dominant organisms         
dom_total = 4*comb(hom,2) + 4*hom*het + 4*hom*rec + 3*comb(het,2) + 2*het*rec

# probability for dominant organisms
phom = dom_total/pop_total
print(phom)
    # probability for dominant organisms + 
    # probability for recessive organisms should be 1
# let's check that:
rec_total = 4 * comb(rec, 2) + 2*rec*het + comb(het, 2)
prec = rec_total/pop_total
print(1 - prec)







from itertools import product

k = 16  # AA  homozygous dominant
m = 30  # Aa  heterozygous
n = 15  # aa  homozygous recessive

population = (['AA'] * k) + (['Aa'] * m) + (['aa'] * n)

all_children = []
for parent1 in population:
    # remove selected parent from population.
    chosen = population[:]
    chosen.remove(parent1)
    for parent2 in chosen:
        # get all possible children from 2 parents. Punnet square
        children = product(parent1, parent2)
        all_children.extend([''.join(c) for c in children])

dominants = filter(lambda c: 'A' in c, all_children)
# float for python2
print (float(len(list(dominants))) / len(all_children))
# 0.7833333

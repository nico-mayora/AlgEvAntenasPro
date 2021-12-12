import matplotlib.pyplot as plt
from pymoo.core.algorithm import Algorithm
from pymoo.visualization.scatter import Scatter
from pymoo.factory import get_problem
from numpy import asarray, vstack
import re

GREEDY = 'out/ParetoGreedy-50x50A.txt'
ALGORITHM = 'out/50x50A-R3-pop75-gen1500.txt'

with open(GREEDY, 'r') as f:
    greedy_lst = re.findall(r'(\d+)/-(\d+)', f.read())

with open(ALGORITHM, 'r') as f:
    alg_lst = re.findall(r'Poblacion: -(\d+), Costo: (\d+)', f.read())


greedy_parsedx = []
greedy_parsedy = []
for e in greedy_lst:
    greedy_parsedx.append(int(e[0])//1000)
    greedy_parsedy.append(int(e[1]))


alg_parsedx = []
alg_parsedy = []
for e in alg_lst:
    alg_parsedx.append(int(e[1])//1000)
    alg_parsedy.append(int(e[0]))

print(alg_parsedx)
print(alg_parsedy)


# plot = Scatter()
# plot.add(alg_parsed, facecolor="none", edgecolor="red")
# plot.show()


plt.figure(figsize=(7, 5))
plt.title('Greedy vs Evolutivo')
plt.scatter(alg_parsedx, alg_parsedy, s=20,
            facecolors='none', edgecolors='blue')
plt.scatter(greedy_parsedx, greedy_parsedy, s=20,
            facecolors='none', edgecolors='red')
plt.show()

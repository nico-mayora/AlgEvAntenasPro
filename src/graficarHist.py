import matplotlib.pyplot as plt
from pymoo.core.algorithm import Algorithm
from pymoo.visualization.scatter import Scatter
from pymoo.factory import get_problem
from numpy import asarray, vstack
import re

CostArch = 'out/SolutionsHistCosto.txt'
PoblArch = 'out/SolutionsHistPobl.txt'

with open(CostArch, 'r') as f:
    cost_lst = re.findall(r'(\d+)\n', f.read())

with open(PoblArch, 'r') as f:
    pobl_lst = re.findall(r'(\d+)\n', f.read())


costo_parsedx = []
for e in cost_lst:
    costo_parsedx.append(int(e))


pobl_parsedy = []
for e in pobl_lst:
    pobl_parsedy.append(int(e))



# plot = Scatter()
# plot.add(alg_parsed, facecolor="none", edgecolor="red")
# plot.show()
dif = []

for i in range(39):
    maxLoc = 0
    minLoc = 1000000
    for j in range(len(costo_parsedx)):
        if costo_parsedx[j] == i:
            if pobl_parsedy[j] > maxLoc:
                maxLoc = pobl_parsedy[j]
            if pobl_parsedy[j] < minLoc:
                minLoc = pobl_parsedy[j]
    dif.append(maxLoc-minLoc)

print(dif)

print((sum(dif))/len(dif))

print((sum(pobl_parsedy))/len(pobl_parsedy))

plt.figure(figsize=(7, 5))
plt.title('Paretos')
plt.scatter(costo_parsedx, pobl_parsedy, s=20,
            facecolors='none', edgecolors='blue')
plt.show()
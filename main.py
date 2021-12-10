from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.population import Population
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.factory import get_termination
from pymoo.optimize import minimize
import numpy as np
from problem import Towers
import matplotlib.pyplot as plt

def readTable():
    
    with open('matriz.txt', 'r') as f:
        M = int(f.readline()[:-1])
        N = int(f.readline()[:-1])
        res = np.zeros((M,N))
        for y in range(M):
            temp = f.readline()
            lista = temp.split(' ')
            for x in range(N):
                res[y, x] = int(lista[x])
        return M, N, res
                

termination = get_termination("n_gen", 1000)

M, N, A = readTable()
costo = 100
rango = 1
problem = Towers(A, 5, costo)

algorithm = NSGA2(
    pop_size=40,
    n_offsprings=10,
    sampling=np.random.randint(2, size=(40, N*M)),
    crossover=get_crossover("bin_ux"),
    mutation=get_mutation("bin_bitflip"),
    eliminate_duplicates=True
)

print('Tabla de poblacion')
print(f'Poblacion Total: {A.sum():.0f}')
for y in range(0,M):
    for x in range(0, N):
        print(f'{A[y,x]:.0f} ', end='')
    print('')

res = minimize(problem,
               algorithm,
               termination,
               save_history=True,
               verbose=True)

X = res.X
F = res.F

pobTot = A.sum()
costoNorm = M*N*costo
with open('Solutions.txt', 'w') as f:
    iter = 0
    for arr in X.astype(int):
        f.write(f'Poblacion: {(pobTot - (F[iter][1]*pobTot)):.0f}, Costo: {F[iter][0]*costoNorm:.0f}\n')
        for y in range(0,M):
            for x in range(0, N):
                f.write(f'{arr[y*N + x]:d} ')
            f.write('\n')
        f.write('\n')
        f.write('\n')
        iter += 1

xl, xu = problem.bounds()
plt.figure(figsize=(7, 5))
plt.scatter(F[:, 0], F[:, 1], s=30, facecolors='none', edgecolors='blue')
plt.title("Objective Space")
plt.show()

#print(res.time)
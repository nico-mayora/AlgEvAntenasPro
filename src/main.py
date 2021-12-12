from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.core.population import Population
from pymoo.factory import get_sampling, get_crossover, get_mutation
from pymoo.factory import get_termination
from pymoo.optimize import minimize
import numpy as np
from problem import Towers
import matplotlib.pyplot as plt

def readTable(direccion):
    with open(direccion, 'r') as f:
        M = int(f.readline()[:-1])
        N = int(f.readline()[:-1])
        res = np.zeros((M,N))
        for y in range(M):
            temp = f.readline()
            lista = temp.split(' ')
            for x in range(N):
                res[y, x] = int(lista[x])
        return M, N, res            

gens = int(input('Ingrese el numero de generaciones: '))
direc = 'instances/' + input('Ingrese el nombre del archivo de instancia: ')
costo = int(input('Ingrese el costo para cada torre: '))
rango = int(input('Ingrese el rango de cada torre: '))
pop = int(input('Ingrese el tamaño de poblacion por generacion: '))

termination = get_termination("n_gen", gens)
M, N, A = readTable(direc)
problem = Towers(A, rango, costo)
init = np.vstack( ( np.zeros((pop//2, N*M)), np.ones((pop//2, N*M)) ) )

algorithm = NSGA2(
    pop_size=pop,
    n_offsprings=10,
    sampling= init,
    crossover=get_crossover("bin_ux"),
    mutation=get_mutation("bin_bitflip"),
    eliminate_duplicates=True
)

res = minimize(problem,
               algorithm,
               termination,
               save_history=True,
               verbose=True)

X = res.X
F = res.F

pobTot = A.sum()
costoNorm = M*N*costo
with open('out/Solutions.txt', 'w') as f:
    iter = 0
    for arr in X.astype(int):
        f.write(f'Poblacion: {F[iter][1]:.0f}, Costo: {F[iter][0]:.0f}\n')
        for y in range(0,M):
            for x in range(0, N):
                f.write(f'{arr[y*N + x]:d} ')
            f.write('\n')
        f.write('\n')
        f.write('\n')
        iter += 1

xl, xu = problem.bounds()
plt.figure(figsize=(7, 5))
plt.scatter(F[:, 0], F[:, 1], s=20, facecolors='none', edgecolors='blue')
plt.title("Soluciones no Dominadas")
plt.show()

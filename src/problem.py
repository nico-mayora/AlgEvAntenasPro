import numpy as np
from pymoo.core.problem import ElementwiseProblem


def printTable(M, N, A):
    print('Tabla de poblacion')
    print(f'Poblacion Total: {A.sum():.0f}')
    for y in range(0,M):
        for x in range(0, N):
            print(f'{A[y,x]:.0f} ', end='')
        print('')


class Towers(ElementwiseProblem):

    def __init__(self, matrPobLoc, rangoLoc, precioLoc):
        self.M = len(matrPobLoc) #altura
        self.N = len(matrPobLoc[0]) #ancho
        self.matriz = matrPobLoc
        self.rango = rangoLoc
        self.precio = precioLoc


        super().__init__(n_var=self.N*self.M,
                         n_obj=2,
                         n_constr=0,
                         xl=0, 
                         xu=1, 
                         type_var=bool)

    def __costo(self, vec):
        tot = 0
        for i in range(0,self.M*self.N):
            if vec[i] == 1:
                tot += self.precio

        return tot


    def __assign(self, x, y):
        if 0 <= x < self.N and 0 <= y < self.M:
            self.matrConteo[y, x] = 1

    def __poblacionTot(self, vec):
        pob = 0
        self.matrConteo = np.zeros((self.M, self.N))
        for y in range(0,self.M):
            for x in range(0, self.N):
                if vec[y*self.N + x] == 1:
                    self.__poblacionParcial(x, y)

        for y in range(0,self.M):
            for x in range(0, self.N):
                pob += self.matriz[y, x]*int(self.matrConteo[y,x])
  
        return pob

    def __poblacionParcial(self, x, y):
        for i in range(self.rango + 1):
            for j in range(self.rango + 1):
                if np.linalg.norm((i, j)) <= self.rango:
                    self.__assign(x + i, y + j)
                    self.__assign(x - i, y + j)
                    self.__assign(x + i, y - j)
                    self.__assign(x - i, y - j)
                else:
                    break
                    

    def _evaluate(self, x, out, *args, **kwargs):
        out["F"] = [self.__costo(x), - self.__poblacionTot(x)]


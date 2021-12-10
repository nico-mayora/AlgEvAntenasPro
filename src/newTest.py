import numpy as np

def readTable(direc):
    with open(direc, 'r') as f:
        M = int(f.readline()[:-1])
        N = int(f.readline()[:-1])
        res = np.zeros((M,N))
        for y in range(M):
            temp = f.readline()
            lista = temp.split(' ')
            for x in range(N):
                res[y, x] = int(lista[x])
        return M, N, res

def readTableFuck(direc):
    with open(direc, 'r') as f:
        M = int(f.readline()[:-1])
        N = int(f.readline()[:-1])
        res = np.zeros(M*N)
        for y in range(M):
            temp = f.readline()
            lista = temp.split(' ')
            for x in range(N):
                res[y*N + x] = int(lista[x])
        return res

def printTable(M, N, A):
    print('Tabla de poblacion')
    print(f'Poblacion Total: {A.sum():.0f}')
    for y in range(0,M):
        for x in range(0, N):
            print(f'{A[y,x]:.0f} ', end='')
        print('')

class Towers():
    def __init__(self, matrPobLoc, rangoLoc, precioLoc, vec):
        self.M = len(matrPobLoc) #altura
        self.N = len(matrPobLoc[0]) #ancho
        self.matriz = matrPobLoc
        self.rango = rangoLoc
        self.precio = precioLoc
        #self.costoNorm = self.M * self.N * self.precio #normalizar
        #self.pobTot = self.matriz.sum()
        self.__poblacionTot(vec)

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
        
        printTable(self.M, self.N, self.matrConteo)

        for y in range(0,self.M):
            for x in range(0, self.N):
                pob += self.matriz[y, x]*self.matrConteo[y,x]

        #pob = (self.pobTot - pob) / self.pobTot
        print(pob)

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

M, N, A = readTable('instances/instance_20x20.txt')
Vec = readTableFuck('instances/kek.txt')
Towers(A, 5, 100, Vec)
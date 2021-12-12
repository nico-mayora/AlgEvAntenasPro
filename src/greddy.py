import numpy as np

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

def valor(x, y, M, N, A):
    if 0 <= x < N and 0 <= y < M:
        return A[y, x]
    return 0

def pobParcial(x, y, M, N, A, rango):
    pob = 0
    for i in range(rango + 1):
        for j in range(rango + 1):
            if np.linalg.norm((i, j)) <= rango:
                if i == 0:
                    if j == 0:
                        pob += valor(x, y, M, N, A)
                    else:
                        pob += valor(x, y + j, M, N, A)
                        pob += valor(x, y - j, M, N, A)
                else:
                    if j == 0:
                        pob += valor(x + i, y, M, N, A)
                        pob += valor(x - i, y, M, N, A)
                    else:
                        pob += valor(x + i, y + j, M, N, A)
                        pob += valor(x - i, y + j, M, N, A)
                        pob += valor(x + i, y - j, M, N, A)
                        pob += valor(x - i, y - j, M, N, A)
            else:
                break
    return pob

def mejorTorre(M, N, A, rango):
    xMax, yMax = 0, 0
    pobMax = 0
    for y in range(0,M):
        for x in range(0, N):
            pob = pobParcial(x, y, M, N, A, rango)
            if pobMax < pob:
                pobMax = pob
                xMax, yMax = x, y
  
    return xMax, yMax, pobMax

def assign(x, y, M, N, A):
    if 0 <= x < N and 0 <= y < M:
        A[y, x] = 0


def removePoblacion(x, y, M, N, A, rango):
    for i in range(rango + 1):
        for j in range(rango + 1):
            if np.linalg.norm((i, j)) <= rango:
                assign(x + i, y + j, M, N, A)
                assign(x - i, y + j, M, N, A)
                assign(x + i, y - j, M, N, A)
                assign(x - i, y - j, M, N, A)
            else:
                break

direc = 'instances/' + input('Ingrese el nombre del archivo de instancia: ')
M, N, A = readTable(direc)
nTorres = int(input('Ingrese el numero torres que desea calcular: '))
costo = int(input('Ingrese el costo de las torres: '))
rango = int(input('Ingrese el rango de las torres: '))
res = np.zeros((M, N))
pobCubierta = 0

for i in range(nTorres):
    print(f'Colocando torre {i + 1}')
    x, y, pobC = mejorTorre(M, N, A, rango)
    removePoblacion(x, y, M, N, A, rango)
    res[y, x] = 1
    pobCubierta += pobC

print(f'Poblacion Cubierta: {pobCubierta}')

with open('out/SolutionsGreddy.txt', 'w') as f:
    f.write(f'Poblacion: {pobCubierta:.0f}, Costo: {costo*nTorres:.0f}\n')
    for y in range(0,M):
        for x in range(0, N):
            f.write(f'{res[y, x]:.0f} ')
        f.write('\n')
    f.write('\n')
    f.write('\n')
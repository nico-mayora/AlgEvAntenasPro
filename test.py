import numpy as np





for y in range(0,20):
    for x in range(0, 20):
        print(f'{A[y,x]:.0f} ', end='')
    print('')

    import numpy as np

N = 50
M = 50

def assign(x, y, valor):
    if 0 <= x < N and 0 <= y < M:
        matris[y, x] = valor


matris = np.zeros((N,M))
rango = 0
px = 5
py = 5
for i in range(rango + 1):
    for j in range(rango + 1):
        if np.linalg.norm((i, j)) <= rango:
            assign(px + i, py + j, 1)
            assign(px - i, py + j, 1)
            assign(px + i, py - j, 1)
            assign(px - i, py - j, 1)


px = 30
py = 30
for i in range(rango + 1):
    for j in range(rango + 1):
        if np.linalg.norm((i, j)) <= rango:
            assign(px + i, py + j, 1)
            assign(px - i, py + j, 1)
            assign(px + i, py - j, 1)
            assign(px - i, py - j, 1)
        else:
            break



for i in range(0,50):
    for j in range(0,50):
        print(f'{matris[i,j]:.0f} ', end='')
    print('')
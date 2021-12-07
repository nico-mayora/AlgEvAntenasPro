from random import randint
import numpy as np
import sys
from sys import exit as halt

MAX_POP = 3
TIGHTNESS = 8  # higher => tighter
WIDTH = 500
HEIGHT = 500
FILE_NAME = 'instance.txt'


def generate(width, height):
    centres = width + height
    line_tol: int = min(width, height) // TIGHTNESS
    mat = np.zeros((width, height))
    indices = [(randint(0, width-1), randint(0, height-1))
               for k in range(centres)]

    conn = [(randint(line_tol-k[0], line_tol+k[0]),
             randint(line_tol-k[1], line_tol+k[1])) for k in indices]
    conn = [(max(min(width - 1, x[0]), 0), max(min(height - 1, x[1]), 0))
            for x in conn]

    conn2 = [(randint(line_tol-k[0], line_tol+k[0]),
             randint(line_tol-k[1], line_tol+k[1])) for k in conn]
    conn2 = [(max(min(width - 1, x[0]), 0), max(min(height - 1, x[1]), 0))
             for x in conn2]

    tot = indices + conn + conn2

    for k in tot:
        mat[k[0], k[1]] = MAX_POP
        for i in range(line_tol // TIGHTNESS):
            for r in range(i + 1):
                for s in range(i + 1):
                    if np.linalg.norm((r, s)) <= i:
                        u = max(min(width - 1, k[0] + r), 0)
                        v = max(min(width - 1, k[0] - r), 0)
                        w = max(min(height - 1, k[1] + s), 0)
                        z = max(min(height - 1, k[1] - s), 0)
                        mat[u, w] += randint(0, MAX_POP // 2)
                        mat[v, w] += randint(0, MAX_POP // 2)
                        mat[u, z] += randint(0, MAX_POP // 2)
                        mat[v, z] += randint(0, MAX_POP // 2)

    return mat


try:
    f = open(FILE_NAME, 'w')
except:
    print('File doesn\'t exist. Please create it before running the script.')
    halt()

print("Generating...")
mat = generate(WIDTH, HEIGHT)
print("Generation finished! Saving to file...")

og_stdout = sys.stdout
sys.stdout = f

print(f'{WIDTH}\n{HEIGHT}')
for t in mat:
    for r in t:
        print(f'{int(r)}', end=' ')
    print('')

sys.stdout = og_stdout
print('Saved!')

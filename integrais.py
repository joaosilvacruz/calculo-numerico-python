import numpy as np


def f(x, y, z):
    f = 12*x*(y**2)*(z**3)
    return f


sol_exata = 648
xi = -1
xf = 2
nx = 100
hx = (xf - xi)/nx

yi = 0
yf = 3
ny = 100
hy = (yf - yi) / ny

zi = 0
zf = 2
nz = 100
hz = (zf - zi)/nz

x = np.linspace(0, 0, nx + 1)
y = np.linspace(0, 0, ny + 1)
z = np.linspace(0, 0, nz + 1)

for i in range(0, nx + 1):
    x[i] = xi + i * hx
for j in range(0, ny + 1):
    y[j] = yi + j * hy
for k in range(0, nz + 1):
    z[k] = zi + k * hz

int_aprox = 0
for i in range(0, nx):
    for j in range(0, ny):
        for k in range(0, nz):
            deltax = (x[i + 1] - x[i])
            deltay = (y[i + 1] - y[i])
            deltaz = (z[i + 1] - z[i])
            deltaV = deltax * deltay * deltaz
            int_aprox = int_aprox + f(x[i + 1], y[j + 1], z[k + 1]) * deltaV

int_aprox1 = 0
for i in range(0, nx):
    for j in range(0, ny):
        for k in range(0, nz):
            deltax1 = (x[i + 1] - x[i])
            deltay1 = (y[i + 1] - y[i])
            deltaz1 = (z[i + 1] - z[i])
            deltaV1 = deltax1 * deltay1 * deltaz1
            xm = x[i] + deltax1/3
            ym = y[i] + deltay1/3
            zm = z[i] + deltaz1/3
            int_aprox1 = int_aprox1 + f(xm, ym, zm) * deltaV 

erro_percentual = (np.abs(sol_exata - int_aprox)/sol_exata)*100
erro_percentual1 = (np.abs(sol_exata - int_aprox1)/sol_exata)*100
print(f"O valor aproximado da integral Tripla com número de partições em x: {nx}; número de partições em y: {ny}; número de partições em z: {nz} é:")
print(f"Com o método sem dividir os deltas {int_aprox} com erro percentual de {erro_percentual}")
print(f"Com o método dividindo os deltas {int_aprox1} com erro percentual de {erro_percentual1}")

if erro_percentual < erro_percentual1:
    print("\nAssim a melhor solução foi o método sem dividir os deltas")
else:
    print("\nAssim a melhor solução foi o método dividindo os deltas")
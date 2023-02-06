#Imports necessários
import matplotlib.pyplot as plt
import numpy as np

#Definindo a função
def f(x,y):
    f = 16 - x**2 - 2 * y**2
    return f

#Partição no eixo X
xi = 0
xf = 2
nx = 1000  
hx = (xf - xi)/nx

#Partição no eixo Y
yi = 0
yf = 2
ny = 1000 
hy = (yf - yi) / ny

#Definindo o espaço de x e y
x  = np.linspace(0, 0, nx + 1)
y  = np.linspace(0, 0, ny + 1)

#Definindo x e y
for i in range(0, nx + 1):
        x[i] = xi + i * hx
for j in range(0, ny + 1):
        y[j] = yi + j * hy

#Cálculo da integral Dupla
int_aprox = 0
for i in range(0, nx):
    for j in range(0, ny):
        deltax = (x[i + 1] - x[i])
        deltay = (y[i + 1] - y[i])
        deltaA = deltax * deltay
        int_aprox = int_aprox + f(x[i + 1], y[j + 1]) * deltaA 

sol_exata = 48
erro_percentual = (np.abs(sol_exata - int_aprox)/sol_exata)*100
print("O valor aproximado da integral é:", int_aprox)
print("O erro percentual na aproximação é:", erro_percentual)
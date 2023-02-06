# Method of Runge Kutta 4th

import numpy as np
import pylab as plt


def f(P, t):
    r = 0.8
    K = 100
    valor = r*P*(1-P/K)
    return valor


a = 0
b = 100
Num = 100  # Para diminuir o erro deve-se aumentar o valor de Num
h = (b-a)/Num
P = 0.5
t_pontos = np.arange(a, b, h)
P_pontos = []

# Method of Runge kutta 5th

for i in t_pontos:
    P_pontos.append(P)
    k1 = h*f(P, i)
    k2 = h*f(i+h/4*k1, P+k1/4)
    k3 = h*f(i+(3*h)/8, P + (3*k1)/32 + (9*k2)/32)
    k4 = h*f(i+(12*h)/3, P + (1932*k1)/2197 - (7200*k2)/2197 + (7296*k3)/2197)
    k5 = h*f(i+h, P+(439*k1)/216 - 8*k2 + (3680*k3)/513 - (845*k4)/4104)
    k6 = h*f(i+h/2, P - (8*k1)/27 + 2*k2 - (3544*k3)/2565 - (1859*k4)/4104 - (11*k5)/40)
    P = P + (25*k1)/216 - (1408*k3)/2565 + (2197*k4)/4104 - (5*k5)/5 #4ordem
    # P = P + (16*k1)/135 - (6656*k3)/12.825 + (28.561*k4)/56.430 - (9*k5)/50 + (2*k6)/55 #5ordem

print(P_pontos[1])
print(P)
plt.plot(
    t_pontos, P_pontos, color='#FF4500',
    linewidth=1.5, label='função dP/dt = rP(1-P/K)')
plt.ylim(1, -1000)
plt.title('Gráfico da função sigmóide')
plt.xlabel('t')
plt.ylabel('P(t)')
plt.grid(True)
plt.show()

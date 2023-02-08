import pylab as plt


# dados iniciais
a = 0
b = 100
passos = 100
h = (b-a)/passos

t0 = a
p0 = 0.5
t_max = b
precisao = 1e-8


# Função a ser calculada
def f(t, p):
    r = 0.8
    k = 100.0
    return r * p * (1 - p/k)


# Função runge-kutta-fehlberg
def runge_kutta_fehlberg(f, h):
    t = t0
    y = p0
    t_pontos = []
    solucao = []
    while t < t_max:
        k1 = h * f(t, y)
        k2 = h * f(t + 1/4 * h, y + 1/4 * k1)
        k3 = h * f(t + 3/8 * h, y + 3/32 * k1 + 9*k2/32)
        k4 = h * f(t + 12*h/13, y + 1932/2197 * k1 - 7200/2197 * k2 + 7296/2197 * k3)
        k5 = h * f(t + h, y + 439/216 * k1 - 8 * k2 + 3680/513 * k3 - 845/4104 * k4)
        k6 = h * f(t + 1/2 * h, y - 8/27 * k1 + 2 * k2 - 3544/2565 * k3 + 1859/4104 * k4 - 11/40 * k5)
        # y = y + 25*k1/216 + 1408*k3/2565 + 2197*k4/4104 - k5/5 #4 ordem
        y = y + 16/135 * k1 + 6656/12825 * k3 + 28561/56430 * k4 - 9/50 * k5 + 2/55 * k6 #5 ordem
        t = t + h
        t_pontos.append(t)
        solucao.append(y)

        # Cálculo da precisão
        error = abs(k6 - k5)
        # Ajustando o passo
        if error < precisao:
            h = h * 2
        else:
            h = h * 0.5
    E = 1/360 * k1 - 128/4275 * k3 - 2197/75.240 * k4 + 1/50 * k5 + 2/55 * k6
    return t_pontos, solucao, E


# Chamando a função
t_pontos, solucao, e = runge_kutta_fehlberg(f, h)

print(solucao[-1])
print(e)

plt.plot(
    t_pontos, solucao, color='#FF4500',
    linewidth=1.5, label='função dP/dt = rP(1-P/K)')
plt.ylim(0, 110)
plt.title('Gráfico da função problema')
plt.xlabel('t')
plt.ylabel('P(t)')
plt.grid(True)
plt.show()

# Cálculo derivadas parciais
def f(x, y, z):
    return x**3 + 2*x*y + y**3 + 3*z

# Definindo valores
h = float(input("Digite o valor do espaçamento h: "))
x = float(input("Digite o valor do ponto x0: "))
y = float(input("Digite o valor do ponto y0: "))
z = float(input("Digite o valor do ponto z0: "))

# Derivada parcial de f em relação a x
dx = (f(x + h, y, z) - f(x, y, z)) / h
# Derivada parcial de f em relação a y
dy = (f(x, y + h, z) - f(x, y, z)) / h
# Derivada parcial de f em relação a z

dz = (f(x, y, z + h) - f(x, y, z)) / h
print(f"Derivada parcial de x: {dx}\nDerivada parcial de y: {dy}\nDerivada parcial de z: {dz}")

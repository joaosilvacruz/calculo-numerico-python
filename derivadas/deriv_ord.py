# Cálculo de Derivadas usando Python
def f(x):
    return x**2-2*x+4


# Definindo valores
h = float(input("Digite o valor do espaçamento h: "))
x0 = float(input("Digite o valor do ponto x0: "))

# Fórmula derivada
derivada = (f(h+x0) - f(x0)) / (x0)
derivada = (f(h) - f(x0)) / (h - x0)

print(f"O valor da derivada no ponto {x0} é: ", derivada)
print(f"O valor da derivada no ponto {x0} é: ", derivada)

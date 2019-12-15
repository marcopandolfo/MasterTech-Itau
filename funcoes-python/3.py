import math

def calcular_comprimento(raio):
    return 2 * raio * math.pi


def calcular_area(raio):
    return (raio ** 2) * math.pi


print(calcular_comprimento(8))
print(calcular_area(8))
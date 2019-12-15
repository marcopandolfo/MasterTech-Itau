def intervalo_de_pares(inicio, fim):
    numeros = []
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            numeros += [num]
    return numeros


print(intervalo_de_pares(1, 10))
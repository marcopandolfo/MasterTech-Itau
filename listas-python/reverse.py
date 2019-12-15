numeros = [1, 2, 3423, 23, 111]
resposta = input('Deseja printar em ordem crescente ou decrescente? \nCrescente (1) Decrescente (2)').upper()
numeros.sort()

if resposta == '1':
    print(numeros)
elif resposta == '2':
    # Inverte a lista
    numeros.sort(reverse=True)
    print(numeros)
else:
    print('Opção invalida')

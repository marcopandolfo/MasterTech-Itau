# 6 - Construa um algoritmo de IMC
peso = float(input('Insira seu PESO: '))
altura = float(input('Insira sua ALTURA: '))

imc = peso / (altura ** 2)

print('============ DADOS ================')
print(f'ALTURA: {altura}')
print(f'PESO: {peso}')
print(f'IMC: {imc}')

if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif imc <= 24.9:
    print('Parabéns! você está no seu peso normal')  
elif imc <= 30:
    print('Você está acima de seu peso (sobrepeso)')
elif imc > 30:
    prinf('Você está Obeso')
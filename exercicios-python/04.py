# holerite entrar com o salário de um colaborador e fazer os cálculos de descontos
# INSS 9%

salario = float(input('Entre com o salario: '))

valor_inss = 0.09 * salario
valor_transporte = 0.03 * salario
valor_saude = 0.15 * 347.00 # valor total do plano

print(f'Salario integral: {salario}\n')
print('==== VALORES DESCONTADOS ====')
print(f'INSS: {valor_inss}')
print(f'TRANSPORTE: {valor_transporte}')
print(f'SAUDE: {valor_saude}')

total_descontado = valor_inss + valor_transporte + valor_saude
salario -= total_descontado
print('==================')
print(f'Salario liquido: {salario}')

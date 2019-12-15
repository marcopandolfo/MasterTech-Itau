# 3 - entre com 4 notas de um aluno e calcule a média. 
# Imprima a situação do aluno de acordo com sua média 
# (média > 7 aprovado, média < 7 e > 5.5 recuperação, demais médias reprovado)

notas = []

for i in range(1, 4):
    nota = float(input(f'Insira sua nota ({i}/4)'))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f'Sua média é {media}')

if media > 7:
    print('Você está aprovado')
elif (media <  7) and (media > 5.5):
    print('Você está de recuperação')
else:
    print('Você está reprovado')
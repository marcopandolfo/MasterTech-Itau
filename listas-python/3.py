nomes = ['Marco', 'Julia', 'Diana', 'Ana', 'Felip']
nomes.sort()
aluno = 0
len_nomes = len(nomes) - 1
letra_u = input('Entre com a letra inicial: ')
while len_nomes != -1:
    if nomes[len_nomes][0].lower() == letra_u:
        print(nomes[len_nomes])
        len_nomes -= 1
        aluno += 1
    else:
        len_nomes -= 1
if aluno == 0:
    print('Não existe aluno com esse inicial na lista')

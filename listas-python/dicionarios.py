pessoa = {
    "nome": 'Joao Silveira Lima',
    "e-mail":'joao@gmail.com'
}
print(f'Bem vindo {pessoa["nome"]}, seu e-mail: {pessoa["e-mail"]}')

# Atualizar valor
pessoa.update({"Ativo": True})
print(pessoa)
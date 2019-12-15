class Funcionario:
    def __init__(self, nome, email, rg, idade, salario):
        self.nome = nome
        self.email = email
        self.rg = rg
        self.idade = idade
        self.salario = salario

    def __str__(self):
        return f'Olá {self.nome}, você foi cadastrado com sucesso em nosso sistema!'

    def aumentar_salario(self, acressimo):
        novo_salario = self.salario + acressimo
        return f'Seu salario aumentou para R${novo_salario:.2f}'


novo_funcionario = Funcionario(
    nome='Joaozinho',
    email='joao@gmaiil.com',
    rg='21.233.123-1',
    idade=26,
    salario=4000
)

print(novo_funcionario)
print(novo_funcionario.aumentar_salario(500))
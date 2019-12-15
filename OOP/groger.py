class Pessoa:
    def __init__(self, nome_completo, idade, saldo):
        self.nome_completo = nome_completo
        self.idade = idade
        self.saldo = saldo

    def __str__(self):
        return f'Nome: {self.nome_completo}; Idade: {self.idade}; Saldo: R${self.saldo:.2f}'

    def saque(self, valor):
        self.valor = valor
        if self.valor > self.saldo and self.valor > 1000:
            return 'Saque nao autorizado'
        else:
            self.saldo -= self.valor
            return f'Saque aprovado. Saldo final: R${self.saldo}'

    def deposito(self, valor):
        self.valor = valor
        if valor > 5000:
            return 'Deposito nao autorizado'
        else:
            self.saldo += self.valor
            return f'Deposito aprovado. Saldo final: R${self.saldo}'

    def emprestimo(self, valor):
        self.valor = valor
        if self.idade < 21 and self.saldo > 1000 and self.valor < (self.saldo*15):
            self.saldo += self.valor
            return f'Emprestimo aprovado. Saldo final: R${self.saldo}'


nova_pessoa = Pessoa(str(input('Nome completo: ')), int(input('Idade: ')), float(input('Saldo: R$')))
while True:
    
    print('''Qual operação gostaria de realizar?:
[1] Saque
[2] Deposito
[3] Emprestimo
[Qualquer outro texto ou número] Sair''')

    opcao_usuario = str(input('Sua resposta: ')).strip()
    if opcao_usuario not in '[1][2][3]':
        break
    else:
        if opcao_usuario in '[1]':
            print(nova_pessoa.saque(float(input('Digite o valor do saque: R$'))))
        elif opcao_usuario in '[2]':
            print(nova_pessoa.deposito(float(input('Digite o valor do saque: R$'))))
        elif opcao_usuario in '[3]':
            print(nova_pessoa.emprestimo(float(input('Digite o valor do saque: R$'))))
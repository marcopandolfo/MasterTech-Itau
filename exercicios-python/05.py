# 5 - sistema mercearia
print('Lojinha Mastertech')

carrinho = []

def adicionarProduto(nome, preco, qtde):
    produto = [nome, preco, qtde]
    carrinho.append(produto)

while True:
    resposta = input(f'Há produtos em seu carrinho? (1) SIM (2) NÃO \n')
    if resposta == '1':
        nome = input('Qual o nome do produto? \n')
        preco = float(input('Qual o preço do produto? \n'))
        qtde = int(input('Qual a quantidade? \n'))
        adicionarProduto(nome, preco, qtde)
    else:
        break

print('Recibo: \n=====================\n')
for compra in carrinho:
    print(f'Nome: {compra[0]}, Quantidade: {compra[2]}, Preço: {compra[1] * compra[2]}')
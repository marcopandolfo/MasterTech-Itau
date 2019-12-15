class Carro:
    def __init__(self, proprietario, modelo, marca, preco, placa):
        self.proprietario = proprietario
        self.modelo = modelo
        self.marca = marca
        self.preco = preco
        self.placa = placa

    def __str__(self):
        return f'Olá {self.proprietario}, seu carro é um {self.modelo} - {self.marca} de placa {self.placa}'


# Instancia um carro
meu_carro = Carro(
    proprietario='Joao Silveira',
    modelo='Fusca',
    marca='Volkswagen',
    preco=4000,
    placa='OWH-1234'
)

print(meu_carro)
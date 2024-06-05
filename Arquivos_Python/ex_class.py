class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.motores = list()
        self.carros = list()

    def fabricador_motor(self, nome, cavalaria):
        self.motores.append(Motor(nome, cavalaria))
    
    def fabricador_carro(self, nome, motor='Sem motor'):
        self.carros.append(Carro(nome, motor))

class Motor:
    def __init__(self, nome, cavalaria) -> None:
        self.nome = nome
        self.cavalaria = cavalaria

class Carro:
    def __init__(self, nome, motor='Sem motor') -> None:
        self.nome = nome
        self.motor = motor

    def movimentar(self, direcao, velocidade):
        print(f'O carro está andando para {direcao} á {velocidade}')

f1 = Fabricante('Toyota')
f1.fabricador_motor('x100',120)
f1.fabricador_carro('Corolla', f1.motores[0])
carro1 = f1.carros[0]
f1.fabricador_carro('yaris')
carro2 = f1.carros[1]
print(carro1.nome, f1.nome, carro1.motor.nome,carro1.motor.cavalaria )

def quest(name,msg, response):
    def bem(f_or_t):
        def saudacao(msg, name):
            return f'{msg}, {name}!'
        print(saudacao(msg, name))
        if f_or_t:
            return 'Quem bom! =]'
    if response == 1:
        return bem(True)
    return 'Que pena, espero que em breve você esteja melhor!'
a = input('Digite seu nome: ')
b = int(input(f'Você esta bem {a}? Sim(1)/Não(0)\nR:'))
print(quest(a,'Oi',b))


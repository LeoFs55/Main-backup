def calculo (n1 , n2):
    def soma(op):
        if op == 1:
            return n1 + n2
        elif op == 2:
            return n1 - n2
        elif op == 3:
            return n1 * n2
        elif op == 4:
            return n1 / n2
        elif op == 5:
            return n1 % n2
        else: 
            return 'Objeto não encontrado'
    return soma
def entradas_a():
    a = input('Digite um numero: ')
    global a_valid
    a_valid = float(a)
    return a_valid
def entrada_b():
    b = input('Digite outro numero: ')
    global b_valid
    b_valid = float(b)
    return b_valid
contador = 1
resultado = 0
while contador >= 0:    
    calculos = calculo(entradas_a(),entrada_b())
    operadores = int(input('Indices de operadores|1+|2-|3*|4/|5%|: '))
    print(calculos(operadores))
    resultado += calculos(operadores)
    entrada = int(input('Deseja continuar calculando? Sim(1)/ Não(2)'))
    if entrada == 1:
        continue
    elif entrada == 2:
        break
    else:
        print('Você é burro?')
    
    






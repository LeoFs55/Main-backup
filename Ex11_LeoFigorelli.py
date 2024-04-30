def num_validation(entrada):
    try:
        num = int(entrada)
        return True, num
    except:
        return False,'O valor inserido não é um número.'
    
def bi_validation(numero):

    tupla_numero = tuple(numero)

    for i in tupla_numero:
        if int(i)>1:
            return False, 'O número inserido não era bínario.'
        else:
            continue
    return True, tupla_numero

def calculo(quant):
    resultado = 0
    tupla_entrada = bi_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(2**(i))
        return f'O número {entrada} é igual a {resultado}'

 
while True:
    entrada = input('Digite um numero binario:')
    if num_validation(entrada)[0]:
        quant = len(entrada)

        if bi_validation(entrada)[0]:
            print(calculo(quant))

        else:
            print(bi_validation(entrada)[1])
            continue

        break
    else:
        print(num_validation(entrada)[1])

        continue


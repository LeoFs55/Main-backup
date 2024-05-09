def binario(num, base):
    if base == 10:
            
        entrada = num
        if num_validation(entrada):
            return int(calculo_dec_p_bi(entrada))
        else:
            return num_validation(entrada)[1]

    elif base == 2:

        entrada = num
        if num_validation(entrada):
            quant = len(str(entrada))

            if bi_validation(entrada)[0]:
                return int(calculo_bi_p_dec(entrada,quant))
            
            else:
                return bi_validation(entrada)[1]
            
        else:
                
            print(num_validation(entrada)[1])
            
from packages.validations import num_validation


def bi_validation(numero):

    tupla_numero = tuple(numero)

    for i in tupla_numero:
        if int(i)>1:
            return False, 'O número inserido não era bínario.'
        else:
            continue
    return True, tupla_numero

def calculo_bi_p_dec(entrada,quant):
    resultado = 0
    tupla_entrada = bi_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(2**(i))
    return resultado

def calculo_dec_p_bi(num):
    if num == '0':
        return num
    binario = ''
    decimal  = int(num)
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2
    return binario

from packages.validations import num_validation


def oct_validation(numero):
    tupla_numero = tuple(numero)

    for i in tupla_numero:
        if int(i)>7:
            return False, 'O número inserido não é Octal.'
        else:
            continue
    return True, tupla_numero

def calculo_dec_p_octal(num):
    if num == '0':
        return 0
    octal = ''
    decimal  = int(num)
    while decimal > 0:
        resto = decimal % 8
        octal = str(resto) + octal
        decimal //= 8
    return octal

def calculo_oct_p_dec(entrada,quant):#Calculo de OCTAL PARA DECIMAL
    resultado = 0
    tupla_entrada = oct_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(8**(i))
    return resultado

def octadecimal(num, base):
    if base == 10:    
        entrada = num
        if num_validation(entrada):
            return int(calculo_dec_p_octal(entrada))
                
        else:
            return num_validation(entrada)[1]

    elif base == 8:
        entrada = num
        if num_validation(entrada):
            quant = len(entrada)

            if oct_validation(entrada)[0]:
                return int(calculo_oct_p_dec(entrada,quant))
            else:
                return oct_validation(entrada)[1]
        else:
            print(num_validation(entrada)[1])
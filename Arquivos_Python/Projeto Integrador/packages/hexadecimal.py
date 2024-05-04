from packages.validations import num_validation

def hex_validation(numero):
    lista_numero = list(numero)
    for ind ,i in enumerate(lista_numero):
        if i == 'a' or i == 'A':
            lista_numero[ind] = 10
        elif i == 'b' or i == 'B':
            lista_numero[ind] = 11
        elif i == 'c' or i == 'C':
            lista_numero[ind] = 12
        elif i == 'd' or i == 'D':
            lista_numero[ind] = 13
        elif i == 'e' or i == 'e':
            lista_numero[ind] = 14
        elif i == 'f' or i == 'F':
            lista_numero[ind] = 15
            
    for i in lista_numero:
        if int(i)>15:
            return False, 'O número inserido não era hexadecimal.'
        else:
            continue
    return True, lista_numero

def calculo_hex_p_dec(entrada,quant):#Calculo de HEXA PARA DECIMAL
    resultado = 0
    tupla_entrada = hex_validation(entrada)[1]

    for ind, i in enumerate(range((quant-1),-1,-1)):
        resultado += int(tupla_entrada[ind])*(16**(i))
    return resultado

def calculo_dec_p_hexa(num):
    if num == '0':
        return 0
    hexa = ''
    decimal  = int(num)
    while decimal > 0:
        resto = decimal % 16
        decimal //= 16
        if resto == 10:
            hexa = 'A'+ hexa
        elif resto == 11:
            hexa = 'B'+ hexa
        elif resto == 12:
            hexa = 'C'+ hexa
        elif resto == 13:
            hexa = 'D'+ hexa
        elif resto == 14:
            hexa = 'E'+ hexa
        elif resto == 15:
            hexa = 'F'+ hexa
        else:
            hexa = str(resto) + hexa

    return hexa

def hexadecimal(num, base):
    if base == 10:    
        entrada = num
        if num_validation(entrada):
            return calculo_dec_p_hexa(entrada)
        else:
            return num_validation(entrada)[1]

    if base == 16:
        entrada = num

        quant = len(entrada)
        if hex_validation(entrada)[0]:
            return int(calculo_hex_p_dec(entrada,quant))

        else:
            return hex_validation(entrada)[1]
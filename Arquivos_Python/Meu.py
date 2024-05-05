resultado_cpf = []
resultado_cpf_calculo = ''
entrada_cpf = ''
cpf_entrada_tratado = ''
def digitos(cpf):
    def first_digit(cpf_int):
        for indice, mult in enumerate(range(10,1,-1)):
            resultado = cpf_int[indice] * mult
            resultado_cpf.append(resultado)
        tupla_resultado_cpf = tuple(resultado_cpf)
        soma = 0
        for i in tupla_resultado_cpf:
            soma += i
        digito1 = (soma*10)%11
        digito1 = 0 if digito1 > 9 else digito1
        return digito1
    def second_digit(cpf_int):
        quant = len(cpf)
        resultado = [cpf_int[indice] * mult for indice, mult in enumerate(range(quant,1,-1))]
        soma = 0
        for i in resultado:
            soma += i         
        digito = ((soma*10)%11)
        digito = 0 if digito > 9 else digito
        return digito
    def validation(cpf_int):
        for indice, mult in enumerate(range(10,1,-1)):
            resultado = cpf_int[indice] * mult
            resultado_cpf.append(resultado)
        tupla_resultado_cpf = tuple(resultado_cpf)
        soma = 0
        for i in tupla_resultado_cpf:
            soma += i
        digito1 = (soma*10)%11
        if digito1 > 9:
            digito1 = 0
        else: 
            digito1 = digito1
        str_digito1 = f'{digito1}'
        cpfcom1digito = cpf_entrada_tratado+str_digito1
        resultado_cpf.clear()
        for indice, mult in enumerate(range(11,1,-1)):
            resultado = entrada(cpfcom1digito)[indice] * mult
            resultado_cpf.append(resultado)
        tupla_resultado_cpf = tuple(resultado_cpf)
        soma = 0
        for i in tupla_resultado_cpf:
            soma += i
        digito2 = (soma*10)%11
        if digito2 > 9:
            digito2 = 0
        else: 
            digito2 = digito2
        str_digito2 = f'{digito2}'
        resultado_cpf_calculo = cpfcom1digito+str_digito2
        if resultado_cpf_calculo == entrada_cpf:
            return f'O CPF {resultado_cpf_calculo} é valido!'
        return f'O CPF {resultado_cpf_calculo} é invalido!'
    if cpf == 9:
        return first_digit
    elif cpf == 10:
        return second_digit
    elif cpf == 11:
        return validation
    else:
        return ''

def somadedigitos(cpf):
    def digito1e2(cpf_int):
        for indice, mult in enumerate(range(10,1,-1)):
            resultado = cpf_int[indice] * mult
            resultado_cpf.append(resultado)
        tupla_resultado_cpf = tuple(resultado_cpf)
        soma = 0
        for i in tupla_resultado_cpf:
            soma += i
        digito1 = (soma*10)%11
        if digito1 > 9:
            digito1 = 0
        else: 
            digito1 = digito1
        str_digito1 = f'{digito1}'
        cpfcom1digito = entrada_cpf+str_digito1
        resultado_cpf.clear()
        for indice, mult in enumerate(range(11,1,-1)):
            resultado = entrada(cpfcom1digito)[indice] * mult
            resultado_cpf.append(resultado)
        tupla_resultado_cpf = tuple(resultado_cpf)
        soma = 0
        for i in tupla_resultado_cpf:
            soma += i
        digito2 = (soma*10)%11
        if digito2 > 9:
            digito2 = 0
        else: 
            digito2 = digito2
        return f'{digito1} e {digito2}'
    return digito1e2
    
    
def entrada(cpf):
    global cpf_list
    cpf_list = []
    for i in cpf:    
        cpf_list.append(int(i))
    global cpf_int
    cpf_int = tuple(cpf_list)
    return cpf_int

def cpf9(cpf):
    cpf_valido = ''
    for i in cpf:
        if len(cpf_valido) == 9:
            break
        cpf_valido += i
    return cpf_valido
def quant(cpf):
    global len_cpf
    len_cpf = len(cpf)
    return len_cpf

def escolhas(esc):
    digito1 = esc == 1
    digito2 = esc == 2
    digito1e2 = esc == 3
    verificar = esc == 4
    global entrada_cpf
    global cpf_entrada_tratado
    if digito1:
        entrada_cpf = input('Digite seu CPF: ').replace('-','').replace('.','')
        entrada(entrada_cpf)
        quant(entrada_cpf)
        cpf = digitos(len_cpf)
        print(f'O primeiro digito de seu CPF é {cpf(cpf_int)}')
    elif digito2:
        entrada_cpf = input('Digite seu CPF: ').replace('-','').replace('.','')
        entrada(entrada_cpf)
        quant(entrada_cpf)
        cpf = digitos(len_cpf)
        print(f'O segundo digito de seu CPF é {cpf(cpf_int)}')
    elif digito1e2:
        entrada_cpf = input('Digite seu CPF: ').replace('-','').replace('.','')
        entrada(entrada_cpf)
        quant(entrada_cpf)
        cpf = somadedigitos(entrada_cpf)
        print(f'O primeiro e o segundo digito de seu CPF é {cpf(cpf_int)}')
    elif verificar:
        entrada_cpf = input('Digite seu CPF: ').replace('-','').replace('.','')
        cpf_entrada_tratado = cpf9(entrada_cpf)
        entrada(cpf_entrada_tratado)
        quant(entrada_cpf)
        cpf = digitos(len_cpf)
        print(f'O segundo digito de seu CPF é {cpf(cpf_int)}')

escolha = input('''O que você deseja saber?
O primeiro digito do seu CPF? Digite 1
O Segundo digito do seu CPF? Digite 2
Os dois digitos do seu CPF? Digite 3
Verificar se seu CPF é valido? Digite 4\nR:''')
escolhas(int(escolha))







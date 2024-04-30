import datetime
pessoa_nao_valida = {
}
pessoa_valida = {
}
def entrada_cadastro():
    name = input('Digite o seu primeiro nome: ')
    sobrenome = input('Digite o seu sobrenome: ')
    nascimento = input('Digite o sua data de nascimento (dd/mm/AAAA): ')
    cpf = input('Digite seu CPF: ')
    return (name, sobrenome, nascimento, cpf)

def name_validation(name):
    name_is_name = name.isalpha()
    name_valid = name.lower() if name_is_name else 'name_invalid'
    return name_is_name ,name_valid
def surname_validation(surname):
    surname_ = surname.replace(' ', '')
    surname_is_surname = surname_.isalpha()
    surname_valid = surname.lower() if surname_is_surname else 'surname_invalid'
    return surname_is_surname ,surname_valid

def age_validation(data):
    data_desformatada = data.replace('/','')
    atual = datetime.datetime.now()
    dia = int(data_desformatada[:2])
    mes = int(data_desformatada[2:4])
    ano = int(data_desformatada[4:])
    ano_str = (data_desformatada[4:])
    quant_ano = len(ano_str)<=4
    age_ = datetime.datetime(ano,mes,dia)
    def data_possible(dia,mes):
        match mes:
            case 1:
                if dia<=1 or dia<=31 and quant_ano:
                    return True
                else:
                    return False
            case 2:
                if dia<=1 or dia<=28  and quant_ano:
                    return True
                else:
                    return False
            case 3:
                if dia<=1 or dia<=31  and quant_ano:
                    return True
                else:
                    return False
            case 4:
                if dia<=1 or dia<=30  and quant_ano:
                    return True
                else:
                    return False
            case 5:
                if dia<=1 or dia<=31 and quant_ano:
                    return True
                else:
                    return False
            case 6:
                if dia<=1 or dia<=30 and quant_ano:
                    return True
                else:
                    return False
            case 7:
                if dia<=1 or dia<=31 and quant_ano:
                    return True
                else:
                    return False
            case 8:
                if dia<=1 or dia<=31 and quant_ano:
                    return True
                else:
                    return False
            case 9:
                if dia<=1 or dia<=30 and quant_ano:
                    return True
                else:
                    return False
            case 10:
                if dia<=1 or dia<=31 and quant_ano:
                    return True
                else:
                    return False
            case 11:
                if dia<=1 or dia<=30 and quant_ano:
                    return True
                else:
                    return False
            case 12:
                if dia<=1 or dia<=31 and quant_ano:
                    return True
                else:
                    return False
    def func_idade(atual, age_):
        d1 = age_
        d2 = atual
        diff = d2 - d1
        days = diff.days
        years, days = divmod(days, 365)
        return years
        
    if data_possible(dia,mes):
        age = True
        idade = func_idade(atual,age_)
    else:
        age = 'invalid-age'
        idade = 'invalid-age'
    return age, idade

def cpf_validation(cpf): #True or False
    cpf_ = cpf.replace('.','').replace('-','')
    if cpf_.isdigit():
        def div_cpf(cpf):
            inter_cpf = {
                'cpf_str':cpf,
                'cpf_int_iteiravel':[],
            }
            for i in cpf[:9]:
                inter_cpf['cpf_int_iteiravel'].append(int(i))
            def cpf_multiplication_digit1(cpf_subdivido):
                cpf = cpf_subdivido
                cpf_multiplicado = 0
                for i, multplicador in enumerate(range(10,1, -1)):
                    cpf_multiplicado += cpf['cpf_int_iteiravel'][i]*multplicador
                resultado1 = ((cpf_multiplicado*10)%11)
                resultado1 = 0 if resultado1 > 9 else resultado1
                cpf['cpf_int_iteiravel'].append(resultado1)
                cpf_multiplicado = 0
                for i, multplicador in enumerate(range(11,1, -1)):
                    cpf_multiplicado += cpf['cpf_int_iteiravel'][i]*multplicador
                resultado2 = ((cpf_multiplicado*10)%11)
                resultado2 = 0 if resultado2 > 9 else resultado2
                cpf['cpf_int_iteiravel'].append(resultado2)
                def comparacao(a,b):    
                    cpf_str = ''
                    for i in a:
                        cpf_str += f'{i}'
                    return (True,cpf_str) if cpf_str == b else (False,cpf_str)
                return comparacao(cpf['cpf_int_iteiravel'], cpf['cpf_str'])
            return cpf_multiplication_digit1(inter_cpf)
        return div_cpf(cpf_)
    else:
        return False
dados_entrada = entrada_cadastro()
pessoa_nao_valida['nome'], pessoa_nao_valida['sobrenome'], pessoa_nao_valida['data_nascimento'], pessoa_nao_valida['cpf'] = dados_entrada
print(pessoa_nao_valida)
print(name_validation(pessoa_nao_valida['nome']))
print(surname_validation(pessoa_nao_valida['sobrenome']))
print(cpf_validation(pessoa_nao_valida['cpf']))
print(age_validation(pessoa_nao_valida['data_nascimento']))
pessoa_valida = {
    'name':name_validation(pessoa_nao_valida['nome']),
    'surname':surname_validation(pessoa_nao_valida['sobrenome']),
    'cpf':cpf_validation(pessoa_nao_valida['cpf']),
    'age':age_validation(pessoa_nao_valida['data_nascimento'])
}
print(pessoa_valida)

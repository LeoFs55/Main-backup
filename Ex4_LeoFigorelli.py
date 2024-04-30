print(f'''
{32*'-'}
    Convesor de Unidades de tempo
{32*'-'}
''')
entrada_A = int(input('Digite quantos anos você tem: '))
entrada_M = int(input('Digite quantos meses após seu aniversário você tem: '))
entrada_D = int(input('Digite quantos dias após seu aniversário você tem: '))
print(f'Você possui ~={entrada_D+(entrada_M*30)+(entrada_A*365)} dias de vida')
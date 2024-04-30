print(f'''
{32*'-'}
    Calculadora de perímetro
{32*'-'}
''')

comprimento = float(input('Digite o comprimento do retângunlo (cm): '))
altura = float(input('Digite a altura do retângulo (cm): '))
perímetro = (comprimento*2)+(altura*2)

print(f'O perímetro de um retângulo com {comprimento}cm de comprimento e {altura}cm é {perímetro:.2f}cm ')

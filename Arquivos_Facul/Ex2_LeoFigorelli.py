print(f'''
{32*'-'}
    Calculadora de comissão salarial 
{32*'-'}
''')

salario = float(input('Digite o valor bruto do salário: '))
comissao = (salario/100*5)
print(f'O valor da comissão baseado no salário de R${salario}, a comissao será de {comissao}. E seu salário será de {(salario+comissao):.2f} ')
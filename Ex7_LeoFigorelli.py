print(f'''
{len('Determinador de classe eleitoral')*'='}
Determinador de classe eleitoral    
{len('Determinador de classe eleitoral')*'='}
''')
idade = input('Digite a sua idade: ')
idadeint = int(idade)
naoeleitor = idadeint<16
eleitor = idadeint>=18 and idadeint<=65
facultativo = idadeint>=16 and idadeint<18 or idadeint>65
if eleitor:
    print('Você precisa votar.')
elif facultativo:
    print('Você não precisa, mas caso queira é bom votar.')
else:
    print('Você ainda não pode votar.')    

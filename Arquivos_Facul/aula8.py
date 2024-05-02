cadastro = input('Digite seu nome, sobrenome, idade, ano de nascimento e altura em metros: ')
print(f'''Nome: {cadastro.split()[0]}
Sobrenome: {cadastro.split()[1]} {cadastro.split()[2]}
Idade: {cadastro.split()[3]} anos
Ano de nascimento: {cadastro.split()[4]}
É maior de idade: {int(cadastro.split()[3])>=18}
Altura: {cadastro.split()[5]}m
''')

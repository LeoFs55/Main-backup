import packages

name = packages.name('Leonardo')
surname = packages.surname('Figorelli Santana')
age = packages.date_validation('28/10/2005')
cpf = packages.cpf('48448072855')
password = packages.password('Senha123!')

print(packages.data_input(name,surname,age,cpf,password))

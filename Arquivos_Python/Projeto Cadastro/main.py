import packages

name = packages.name('Leo3ardo')
surname = packages.surname('Figo1elli Santana')
age = packages.date_validation('38/10/2005')
cpf = packages.cpf('48448082855')
password = packages.password('Senha123')

packages.data_input(name,surname,age,cpf,password)

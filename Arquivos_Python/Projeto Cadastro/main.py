import packages

name = 'Leonardo'
surname = 'Figorelli Santana'
age = '28/10/2005'
cpf = packages.cpf('48448072855')

with open('Arquivos_Python\Projeto Cadastro\dados.txt','a') as pagina:
    pagina.write(f"""
    'nome':{name},
    'sobrenome':{surname},
    'data-nascimento':{age},
    'cpf':{cpf},
""")

def data_input(name,surname,age,cpf,password):
    with open('Arquivos_Python\Projeto Cadastro\dados.txt','a') as pagina:
        pagina.write(f"""
    'nome':{name},
    'sobrenome':{surname},
    'data-nascimento':{age},
    'cpf':{cpf},
    'senha':{password}
""")
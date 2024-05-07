def data_input(name,surname,age,cpf,password):
    with open('Arquivos_Python\Projeto Cadastro\dados.txt','r+') as pagina:
        if cpf not in pagina.read():    
            pagina.write(f"""
    'nome':{name},
    'sobrenome':{surname},
    'data-nascimento':{age},
    'cpf':{cpf},
    'senha':{password}
""")
            return 'Usuário cadastrado'
        else: 
            return 'Usuário já cadastrado.'
import packages
import mysql.connector
import pprint

import packages.data_input
name = 'Leonardo'
surname = 'Figorelli Santana'
birth = '28/10/2005'  # A data precisa estar no formato 'YYYY-MM-DD' para ser inserida corretamente no MySQL
cpf = '48448072855'
password = 'Senha123!'
email = 'leofigorelli@gmail.com'
def entrada(name,surname,birth,cpf,password,email):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='1234',
        database='bd_project',
    )

    cursor = conexao.cursor()
    sql = "INSERT INTO cadastro (name, surname, birth, cpf, `email`, password) VALUES (%s, %s, %s, %s, %s, %s)"
    val = packages.data_input.data_recb(name,surname,birth,cpf,password,email) # Corrigido para incluir todos os valores
    print(val)
    cursor.execute(sql, val)
    conexao.commit()
    cursor.close()
    conexao.close()

entrada(name, surname, birth, cpf,password, email)
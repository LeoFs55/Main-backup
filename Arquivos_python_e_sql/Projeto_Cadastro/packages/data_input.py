import packages.password_validation as password_validation
import packages.name_validation as name_validation
import packages.age_validation as age_validation
import packages.cpf_validation as cpf_validation
import packages.email_validation as email_validation
import packages.formatting as formatt
import mysql.connector

conexao = mysql.connector.connect(host='localhost',user='root',password='1234',database='bd_project',)
cursor = conexao.cursor()

def rep_user(cpf):
    cursor.execute(f'SELECT cpf FROM cadastro')
    cpfs = [linha[0] for linha in cursor.fetchall()]
    return cpf not in cpfs

def entrada(name,surname,birth,cpf,password,email):
    if rep_user(cpf):
        sql = "INSERT INTO cadastro (name, surname, birth, cpf, password, `email`) VALUES (%s, %s, %s, %s, %s, %s)"
        val = formatt.data_recb(name,surname,birth,cpf,password,email) # Corrigido para incluir todos os valores
        cursor.execute(sql, val)
        conexao.commit()
        cursor.close()
        conexao.close()
    else:
        print('usuário já cadastrado')


    

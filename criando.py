import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='bd_project',
)

cursor = conexao.cursor()

sql = "INSERT INTO cadastro (name, surname) VALUES (%s,%s)"
# val = (nome,surname)
# cursor.execute(sql,val)

conexao.commit()

print(cursor.rowcount,'inserido')



cursor.close()
conexao.close()
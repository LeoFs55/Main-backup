import mysql.connector as connector

def conectar():
    global connection
    connection = connector.connect(host='localhost', user='root', password='1234', database='bd_project')
    global control
    control = connection.cursor()
    
def extraction_login(self):  # Adicionando self como primeiro parâmetro
    self.extraction = self.control.execute("SELECT cpf, email, password FROM cadastro")
    lista = self.control.fetchall()
    return lista

def close():  # Método para fechar a conexão
    if connection.is_connected():
        control.close()
        connection.close()

extraction_instance = 'dads'
result = extraction_instance.extraction_login()
for row in result:
    print(row)
extraction_instance.close()
# Não esqueça de fechar a conexão após o uso
# extraction_instance.close_connection()
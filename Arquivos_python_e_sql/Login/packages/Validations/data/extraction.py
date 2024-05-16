import mysql.connector as connector

class Extraction_db:
    def __init__(self):
        self.connection = connector.connect(host='localhost', user='root', password='1234', database='bd_project')
        self.control = self.connection.cursor()

    def extraction_login(self):  # Adicionando self como primeiro parâmetro
        self.control.execute("SELECT cpf, email, password FROM cadastro")
        lista = self.control.fetchall()
        return lista

extraction_instance = Extraction_db()
result = extraction_instance.extraction_login()
print(result)
# Não esqueça de fechar a conexão após o uso
# extraction_instance.close_connection()
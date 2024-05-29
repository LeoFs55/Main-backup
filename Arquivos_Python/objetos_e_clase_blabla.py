class Usuario:
    def __init__(self):
        self.nome = str()
        self.sobrenome = str()
        self.data_nascimento = str()
        self.cpf = str()
        self.senha = str()
        self.validado = bool()

    def formaterInfoToSQL(self):
        name = self.nome
        surname = self.sobrenome
        birth = self.data_nascimento
        cpf = self.cpf
        password = self.senha
        email = 'leofigorelli@gmail.com'
        return (name, surname, birth, cpf,email, password)

    def register(self,nome,sobrenome,data_nascimento,cpf,password):
        if validations(nome,data_nascimento,cpf,password):
            self.nome = inputFormat(nome,tipo='name')
            self.sobrenome = inputFormat(sobrenome,tipo='name')
            self.data_nascimento = inputFormat(data_nascimento,tipo='birth')
            self.cpf = inputFormat(cpf,tipo='name')
            self.senha = password
            self.validado = True
            usuario = {
                'name': self.nome,
                'surname':self.sobrenome,
                'birth': self.data_nascimento,
                'cpf': self.cpf,
                'password': self.senha,
                'user-valid': self.validado,
            }
            return usuario
        else:
            self.validado = False
    
    def login(self,cpf,password,dictQuarry):
        for i in dictQuarry:
            if i['cpf'] == cpf:
                return True if password == i['password'] else False
            
from datetime import date

def validations(nome, data_nascimento, cpf, password):

    def nomeValid(nome):
        nameList = [i.isalpha() for i in nome.split(' ')]
        if False in nameList:
            return False
        firstName = nome.split()[0]
        repFirstName = firstName[0]*len(firstName)
        if firstName == repFirstName:
            return False
        return True
    
    def dataValid(data_nascimento):
        dia,mes,ano = data_nascimento.split('/')
        dia_int, mes_int, ano_int = int(dia), int(mes), int(ano)

        try:
            valition = date(ano_int, mes_int, dia_int)
            return True
        
        except:
            return False

    def cpfValid(cpf):

        if not cpf.isnumeric():
            return False
        
        resultado = [int(cpf[indice]) * mult for indice, mult in enumerate(range(10,1,-1))]
        soma = sum(resultado)        
        digito = ((soma*10)%11)
        digito = 0 if digito > 9 else digito
        digito1 = str(digito)

        resultado = [int(cpf[indice]) * mult for indice, mult in enumerate(range(11,1,-1))]
        soma = sum(resultado)        
        digito = ((soma*10)%11)
        digito = 0 if digito > 9 else digito
        digito2 = str(digito)

        cpfCriado = cpf[:9]+digito1+digito2

        return True if cpfCriado == cpf else False
    
    def passwordValid(password):
        
        first = password[0].isupper()
        if not first:
            return False
        
        quant = len(password)
        if quant<7:
            return False
        
        special = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/','_','+']
        for i in special:
            if i in password:
                return True

    allValid = nomeValid(nome) and dataValid(data_nascimento) and cpfValid(cpf) and passwordValid(password)
    return allValid

def inputFormat(input, tipo):

    if tipo == 'name':
        return input.lower()
    
    if tipo == 'birth':
        dia,mes,ano = input.split('/')
        dia_int, mes_int, ano_int = int(dia), int(mes), int(ano)
        return f'{ano_int}-{mes_int}-{dia_int}'
 

data = {'nome': 'leonardo', 'sobrenome': 'figorelli santana', 'data_nascimento': '28/10/2005', 'cpf': '48448072855', 'password': 'Senha123!'}
user = Usuario()
user.register(**data)
 
# if usuario1 != False:
#     connectionSQL = ConnectioSql()
#     dictLogin = connectionSQL.extration('cpf, password')
#     listCpf = [i['cpf'] for i in dictLogin]

#     if user.cpf not in listCpf: 
#         connectionJson = ConnectionJson()
#         caminho = connectionJson.nameChanger('treino.json')
#         pessoas = connectionJson.reader(caminho)
#         connectionJson.writer(user.__dict__, caminho, pessoas)

#         connectionSQL = ConnectioSql()
#         tupleForSql = user.formaterInfoToSQL()
#         connectionSQL.writer(tupleForSql)
#     else:
#         print('Usuario já cadastrado')

# else:
#     print('Usuario não cadastrado')
print(user.__dict__)

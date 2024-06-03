# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta1:
    def __init__(self, cor):
        self.tonalidade = cor#somente asim existe a possibilidade de futuramente o dev querer
        #mudar o nome do atributo e se for modificado diretamento no init é possivel ter uma 
        #quebra de código no código cliente
caneta1 = Caneta1('Azul')
# print(caneta1.cor) ->> quebra

class Caneta2:
    def __init__(self, cor):
        self.cor = cor
        self.nome = None
#esse é um setter
    def set_nome(self, user):
        self.nome = user

#esse é um getter
    def get_cor(self):
        return self.cor
caneta2 = Caneta2('Azul')
# print(caneta2.get_cor())
    
#ta isso é diferente
class Caneta3:
    def __init__(self, cor, id):
        self._cor = cor #atributos com _ ou __ não devem ser usados fora do escopo da classe
        self.id = id #aq ele está executando o setter desde o inicio init->setter-> property -> resposta

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        self._cor = valor

    @property
    def id(self):
        return self._codigo
    
    @id.setter
    def id(self,valor):
        self._codigo = valor

    
# caneta3 = Caneta3('Azul',345)
# caneta3.cor = 'Rosa'
# print(caneta3.id)
# print(caneta3.cor)
class Pessoa:
    def __init__(self,name, birth, cpf):
        self.name = name
        self.birth = birth
        self.cpf = cpf

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name.isalpha():
            self._name = name
        else:
            self._name = None
            raise ValueError

    @property
    def birth(self):
        return self._birth
        
    @birth.setter
    def birth(self,birth):    
        self._birth = birth

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self,cpf):
        try:
            if cpf.isnumeric() and cpfValid(cpf):
                self._cpf = cpf
        except ValueError:
            self._cpf = None

    def register(self, name,birth,cpf):
        atributos = [('name',name),('birth',birth),('cpf',cpf)]
        for atributo, valor in atributos:
            setattr(self, atributo, valor)

def cpfValid(cpf):

    if not cpf.isnumeric():
        return False
            
    listInd = [10,11]
    cpf_base = cpf[:9]
    for i in listInd:
        resultado = [int(cpf[indice]) * mult for indice, mult in enumerate(range(i,1,-1))]
        soma = sum(resultado)        
        digito = ((soma*10)%11)
        digito = 0 if digito > 9 else digito
        cpf_base += str(digito)
    return True if cpf_base == cpf else False

user = Pessoa('leonardo', '28/10/2005', '48448072855')
print(user.birth)


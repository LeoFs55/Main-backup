class Pessoa:
    ano = 2023 #atributo de classe, sempre vai ser a mesma coisa pra

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls):
        print('oi')
    
    @classmethod#isso seria um method que cria uma uma class então caso seja necessario
    #definir alguma coisa antes que ele seja objetificado como um nome padrão, sla
    #é só utilizar esse decorador 
    def pessoa_50(cls,nome):
        return cls(nome,50)
pessoa = Pessoa('joão', 23)
print(pessoa.nome)
print(pessoa.idade)
pessoa = Pessoa.pessoa_50('joão')
print(pessoa.nome)
print(pessoa.idade)
# print(Pessoa.ano)
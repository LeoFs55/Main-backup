def soma(x,y):
    # def soma_com(y):
    return x+y
    return soma_com

def multiplica(x,y):
    # def multiplicando(y):
    return x*y
    return multiplicando

def executa(funcao,x):
    def clouser(*args):
        return funcao(x,*args)
    return clouser



soma_com_cinco = executa(soma, 5)
print(soma_com_cinco(6))
multiplica_por_dez = executa(multiplica,10)
print(multiplica_por_dez(6))

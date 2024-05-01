# Raise 
# raise TypeError('Voce é BURRO! Vai fazer outra coisa.')
def somar(n1,n2):
    if validacao_num(n1) and validacao_num(n2):
        return n1 + n2    
    else:
        try:
            raise TypeError(f'O valor "{n1}" ou "{n2}" estão em tipos diferentes')
        except TypeError as error:
            return f'Nome:{error.__class__.__name__} Erro:{error}'    

def validacao_num(n):
    return (True if isinstance(n,(int, float)) else False)

print(somar(10,2))
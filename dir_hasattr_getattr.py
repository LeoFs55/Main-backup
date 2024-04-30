#dir, hasattr e getattr
#dir checa todos o methods possiveis
string = 'Leo'
metodo = 'upper'

if hasattr(string, metodo):#pesquisa diretamente um metodo retonando false our true
    print('Existe')
    print(getattr(string, metodo)())#retonar o metodo que vc atribuiu ao segundo argumento
else:
    print('Não existe o metodo', metodo)

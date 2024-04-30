#con versão de tipos
#tambem conhecido por convertion, typecasting, coercion
print(1+1)
print('a'+'b')
#print('1'+1) vai dar erro pois só existe concatenção com objetos de mesmo tipo
#python é uma linguagem de tipagem forte pq ele nunca muda uma tipagem por vontade própria
#e esses tipos até agora são imutaveis
# só podem ser alteras usando funções como o int, str, bool e float
print(int('1')+1)
print(float('1')+1)
print(bool(0) or True)
print(bool(0) and True)
print('ab'+str(1))
#operadores aritméticos e precedencia
#+
print('Adição: 10 + 10 =',10+10) 
#-
print('Subtração: 10 - 5 =',10-5)
#*
print('Multiplicação: 10 * 10 =',10*10) # Sempre retorna numero float independente do que esteja usando 
#/
print('Divisão: 10 / 4 =',10/4)
#//
print('Divisão inteira: 10 // 4 =',10//4)
#**
print('Exponenciação: 10 ** 2 =',10**2)
#%
print('Módulo: 10 % 3 =',10%3)# Resto de uma divisão inteira
#()
print(2+1-1*2/2**5+5) # A ordem é a seguinte '()' -> '**' -> '*' '/' '//' '%' -> '+' '-'
print(((((2+1)-1)*2)/2)**(5+5))
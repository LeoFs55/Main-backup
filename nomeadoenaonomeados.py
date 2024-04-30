# def soma(x,y,z):
#     #Definição
#     print(f'{x=} {y=} {z=}','|','x + y =',x+y+z)

# soma(1,2,)
# soma(89,29,)#Argumentos não nomeados/ aq tem que ser seguido a ordem
# soma(72, y=29,z=89)#Argumentos nomeados/ aq a ordem pouco importa
# soma(29, y=89, 5)#Argumentos nomeados/ aq a ordem pouco importa
#evitar misturar mas quando misturar se consciencia q os argumentos que vierem dps do nomeado tem que ser nomeados tambem
#refator o código: editar o código
def soma (x,y, z=None):#definindo um não valor / todo paramentro q for definido não pode ter um parametro não definido apos ele
    if z is not None:#def soma (x,y, z=None,k)XXXX
        print(f'{x=} {y=} {z=} =', x + y + z)
    else:
        print(f'{x=} {y=} =', x + y)

soma(1,2)
soma(1213,23)
soma(131234,2512523,12)
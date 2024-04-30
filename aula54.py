# # Ex1
# num = input('Digite um numero inteiro: ')
# try:
#     num_int = int(num)
#     num_par = num_int%2 == 0
#     if num_par:
#         print(f'O número {num_int} é par!')
#     else:
#         print(f'O número {num_int} é impar!')
# except:
#     print('Você não digitou um número.')
# Ex2
# hora = input('Informe a somenta a hora do dia em que você se encontra: ')
# try:
#     hora_int = int(hora)
#     manha = hora_int<=11
#     tarde = hora_int>=12 and hora_int<=17
#     noite = hora_int>=18 and hora_int<=23
#     if manha:
#         print('Bom dia!')
#     elif tarde:
#         print('Boa Tarde!')
#     elif noite:
#         print('Boa Noite!')
#     else:
#         print('Você não digitou um horaio compativel.')
# except:
#     print('Você não digitou um horario')
# Ex3
# nome = input('Digite seu primeiro nome: ')
# nome_p = len(nome)<=4 
# nome_m = len(nome)>=5 and len(nome)<=6
# nome_g = len(nome)>6
# if nome_p:
#     print(f'{nome}, seu nome é pequeno!')
# elif nome_m:
#     print(f'{nome}, seu nome possui um tamanho médio!')
# elif nome_g:
#     print(f'{nome}, seu nome é grande!')

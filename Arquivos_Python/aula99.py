# from sys import path
# from Aula99_package.modulo import somar,subtrair #dessa forma só é possivel se o main estiver na mesma instancia do que o a pasta que o modulo está
# from Aula99_package import modulo #dessa forma só é possivel se o main estiver na mesma instancia do que o a pasta que o modulo está
# import Aula99_package.modulo #dessa forma só é possivel se o main estiver na mesma instancia do que o a pasta que o modulo está
# from Aula99_package.modulo import * #como eu defini o "__all__" o pythom irá importar o que está definido nela
# print(somar(12,23))
# print(modulo.somar(12,23))
# print(Aula99_package.modulo.somar(12,23))
# # print(val)
# print(__name__)
# #E outro adendo, se o modulo importado estiver importando outro modulo, este import deverá ter o endeço como por ex: aula99_package.x_modulo e tambem o arquivo q vc fez isso não pode ser executado
# print(subtrair(10,-2))

import Aula99_package as a99

print(a99.somar(12,4))
lista = [10, 1010, 1111, 11]
for i in lista:
    print(a99.binario(i,2))



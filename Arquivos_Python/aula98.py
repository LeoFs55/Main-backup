#modulos python são singleton(apartir do momento que voce adiciona uma vez, ja foi carregado e coisas que apareceram uma vez
#não vão aparecer dnv)
# import modularizacao
import modularizacao

# for i in range(5):
#     import modularizacao

#Tipo isso ^
# Mas isso é recaregar o modulo
import importlib
bla = importlib.reload
bla(modularizacao)

# for i in range(5):
#     bla(modularizacao)

# tendeu? =D
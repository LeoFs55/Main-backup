from itertools import combinations,permutations, product
from pprint import pprint
pessoas = ['Joao','Joana','Luiz','Leticia']
camisetas = [['preta','branca'],['p','m','g'],['masculino','feminino','unisex'],['algodao','poliester']]
# pprint(list(combinations(pessoas,2)))
# pprint(list(permutations(pessoas,2)))
pprint(list(product(*camisetas)))
# camisetas_brancas = [i for i in product(*camisetas) if 'branca' in i ]
# camisetas_pretas = [i for i in product(*camisetas) if 'preta' in i ]
# print(camisetas_brancas,'\n',end='\n')
# print(camisetas_pretas,end=' ')
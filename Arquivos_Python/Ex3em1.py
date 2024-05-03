from copy import deepcopy
import arq_package as ap

lista_novos_precos = ap.alteracao_de_preco(ap.produtos)

lista_dict_por_preco = ap.organizador_por_preco(ap.alteracao_de_preco(ap.produtos))

lista_dict_por_nome = ap.organizador_por_nome(ap.alteracao_de_preco(ap.produtos))

print('')

ap.mostrar_lista_de_dicts(lista_novos_precos)

print('')

ap.mostrar_lista_de_dicts(lista_dict_por_nome)

print('')

ap.mostrar_lista_de_dicts(lista_dict_por_preco)
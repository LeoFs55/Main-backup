from copy import deepcopy
import arq_package as ap

lista_novos_precos = ap.alteracao_de_preco(ap.produtos)

lista_dict_por_preco = ap.organizador_por_preco(ap.alteracao_de_preco(ap.produtos))

lista_dict_por_nome = ap.organizador_por_nome(ap.alteracao_de_preco(ap.produtos))

ap.mostrar_lista_de_dicts(ap.produtos)

print('Novo Preço')

ap.mostrar_lista_de_dicts(lista_novos_precos)

print('Por Nome')

ap.mostrar_lista_de_dicts(lista_dict_por_nome)

print('Por Preço')

ap.mostrar_lista_de_dicts(lista_dict_por_preco)

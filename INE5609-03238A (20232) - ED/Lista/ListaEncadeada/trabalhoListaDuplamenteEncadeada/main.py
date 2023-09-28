from lista_duplamente_encadeada import Lista


lista = Lista()

print('Instanciando 33 como primeiro elemento da lista')
lista.primeiro_elemento(33)
lista.buscar(33)
print(lista.acessar_atual().chave)
print(lista.listar_lista())

print('\nInserindo 11 como primeiro')
lista.inserir_como_primeiro(11)
lista.buscar(11)
print(lista.acessar_atual().chave)
print(lista.listar_lista())

print('\nInserindo 99 como ultimo')
lista.inserir_como_ultimo(99)
lista.buscar(99)
print(lista.acessar_atual().chave)
print(lista.listar_lista())

print('\nInserindo 88 antes do 99')
lista.buscar(99)
lista.inserir_antes_do_atual(88)
lista.buscar(88)
print(lista.acessar_atual().chave)
print(lista.listar_lista())

print('\nInserindo 22 apos o 11')
lista.buscar(11)
lista.inserir_apos_atual(22)
lista.buscar(22)
print(lista.acessar_atual().chave)
print(lista.listar_lista())

print('\nInserindo 44 na posicao 4')
lista.inserir_na_posicao(4, 44)
lista.buscar(44)
print(lista.acessar_atual().chave)
print(lista.listar_lista())

print('\nExcluir elemento da posicao 4 (44)')
lista.excluir_da_posicao(4)
print(lista.listar_lista())

print('\nBuscando e excluindo o 99')
lista.buscar(99)
lista.excluir_atual()
print(lista.listar_lista())

print('\nExcluindo primeiro elemento (11)')
lista.excluir_primeiro()
print(lista.listar_lista())

print('\nExcluindo ultimo elemento (88)')
lista.excluir_ultimo()
print(lista.listar_lista())

print('\nExcluindo o elemento 22 pela chave')
lista.excluir_elemento(22)
print(lista.listar_lista())

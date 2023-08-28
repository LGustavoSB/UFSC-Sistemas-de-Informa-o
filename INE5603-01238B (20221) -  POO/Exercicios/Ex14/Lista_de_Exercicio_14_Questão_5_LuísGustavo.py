def valida_num_numeros(qtd_numeros):
	while not 0 <= qtd_numeros <= 10**5:
		qtd_numeros = int(input('Valor Inválido. Tente Novamente: '))
	return qtd_numeros


def valida_tamanho_lista(lista):
	while len(lista) != num_numeros:
		lista = input('Quantidade de numeros diferente da informada, Tente novamente: ').split(' ')
	return lista	

def testa_isolados():
	lista_isolados = []
	for i in range(len(lista_numeros)):
		num = lista_numeros.count(lista_numeros[i])
		if num % 2 != 0:
			if lista_numeros[i] in lista_isolados:
				continue
			lista_isolados.append(lista_numeros[i])
	if len(lista_isolados) == 0:
		return 'Nenhum'
	else:
		return lista_isolados

while True:
	
	num_numeros = valida_num_numeros(int(input('Quantos números serão adicionados? ')))
	if num_numeros == 0:
		break
	
	lista_numeros = valida_tamanho_lista(input('Lista: ').split(' '))
	
	isolados = testa_isolados()
		
	print(f'\nNumeros Isolados: {isolados}\n')
	
print('\nFIM DE EXECUÇÃO')
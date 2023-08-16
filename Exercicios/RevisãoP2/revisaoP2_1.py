def main(num_candidatos):
	for i in range(num_candidatos):
		candidato = {}
		candidato['nome'] = input('Nome: ')
		candidato['poder'] = teste_nivel_poder()
		
		
		candidatos.append(candidato)


def teste_num_candidatos():
	while True:
		num_candidatos = int(input('Quantos candidatos serão cadastrados?: '))
		if not 0 <= num_candidatos <= 100:
			print('NUMERO DE CANDIDATOS INVALIDO, [1 <= numero de candidatos <= 100] ou [0] para parar')
			continue
		break
	return num_candidatos


def teste_nivel_poder():
	while True:
		poder = int(input('Poder: '))
		if not 1 <= poder <= 100:
			print('NIVEL DE PODER INVALIDO, [1 <= nivel de poder <= 100]')
			continue
		break
	return poder


def compara_candidatos():
	maior_godofor = 0
	menor_nome = '-'*35
	candidatos_empatados = []
	for candidato in candidatos:
		if candidato['poder'] > maior_godofor:
			nome_godofor = candidato['nome']
			maior_godofor = candidato['poder']
			candidatos_empatados.append(candidato['nome'])
		elif candidato['poder'] == maior_godofor:
			candidatos_empatados.append(candidato['nome'])
			for candidato in candidatos_empatados:
				if len(candidato) < len(menor_nome):
					menor_nome = candidato
			nome_godofor = menor_nome	
	return nome_godofor, maior_godofor



while True:
	candidatos = []
	print('-='*5,'TORNEIO DO PODER','-='*5,'\n')
	
	num = teste_num_candidatos()
	if num == 0:
		break
	
	main(num)
	
	if num == 1:
		godofor = candidatos[0]['nome']
		poder_godofor = candidatos[0]['poder']
	else:
		godofor, poder_godofor = compara_candidatos()
	
	print(f'\nO novo Godofor será {godofor} com {poder_godofor} de poder')


print('\n','-='*5,'FIM DO TORNEIO','-='*6)
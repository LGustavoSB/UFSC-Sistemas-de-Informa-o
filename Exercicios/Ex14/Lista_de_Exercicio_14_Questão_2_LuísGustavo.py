def espaco():
	esp = '-='*35
	return esp


def chamada_original():
	for i in range(num_alunos):
		alunos['nome'] = input("Nome do Aluno: ").capitalize()
		alunos['assinatura'] = input("Assinatura Original: ")
		lista_alunos.append(alunos.copy())


def chamada_aula():
	for i in range(alunos_presentes):
		chamada['nome'] = input("Nome do aluno: ").capitalize()
		chamada['assinatura'] = input("Assinatura da Aula: ")
		lista_chamada.append(chamada.copy())


def valida_num_alunos(qtd_alunos):
	while not 0 <= qtd_alunos <= 50:
		qtd_alunos = int(input('Quantidade Inválida. Tente outro Número: '))
	return qtd_alunos
	

def valida_assinatura():
	num_falsificadas = 0
	for a in lista_alunos:
		num_erros = 0
		for i in lista_chamada:
			if a['nome'] == i['nome']:
				for l in range(len(a['nome'])):
					if (a['assinatura'])[l] != (i['assinatura'])[l]:
						num_erros += 1
		if num_erros > 1:
			num_falsificadas += 1
			alunos_falsificadores.append(a['nome'])
	if len(alunos_falsificadores) == 0:
		alunos_falsifcadores = 'Nenhum'
	return num_falsificadas, alunos_falsificadores
	

while True:
	alunos_falsificadores = []
	lista_alunos = list()
	alunos = dict()
	lista_chamada = list()
	chamada = dict()
	
	num_alunos = valida_num_alunos(int(input("Quantos alunos existem na sala? [0/50]: ")))
	
	if num_alunos == 0:
		break
	
	chamada_original()
	
	print(espaco())
	
	alunos_presentes = valida_num_alunos(int(input("Quantos alunos estavam presentes na aula? [0/50]: ")))
	
	chamada_aula()
	
	num_falsificadas, alunos_falsificadores = valida_assinatura()
		
	print(espaco())
	
	print(f"\nForam falsificadas {num_falsificadas} assinaturas.\nOs alunos que falsificaram suas assinaturas foram: {alunos_falsificadores}\n")

print(f'{espaco()}\nFIM DE EXECUÇÃO')
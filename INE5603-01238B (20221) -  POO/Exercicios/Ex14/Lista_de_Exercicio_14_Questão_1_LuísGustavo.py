def espaco():
	esp = '-='*35
	return esp

lista_traducoes = list()
lista_pessoas = list()

num_traducoes = int(input("Quantas traduções de Feliz Natal serão cadastradas? "))

for i in range(num_traducoes):
	traducao = dict()
	traducao['lingua'] = input("Lingua: ")
	traducao['frase'] = input("Tradução: ")
	
	lista_traducoes.append(traducao)
print(espaco())
num_criancas = int(input("Quantas crianças receberão cartas? "))

for i in range(num_criancas):
	pessoa = dict()
	pessoa['nome'] = input("Nome da criança: ")
	pessoa['lingua'] = input("Lingua materna: ")
	
	lista_pessoas.append(pessoa)
print(espaco())
for p in lista_pessoas:
	for t in lista_traducoes:
		if p['lingua'] == t['lingua']:
			print(p['nome'])
			print(t['frase'])
			break
print(espaco())		
print('Fim de Execução')
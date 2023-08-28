def conta_duracao(comp):
	total = 0
	for i in comp:
	    valor = 0
	    for j in i:
	        valor += nota[j]
	        if valor > 64:
	            break
	    if valor == 64:
	        total += 1
	return total

nota = {'W' : 64, 'H' : 32, 'Q' : 16, 'E' : 8, 'S' : 4, 'T' : 2, 'X' : 1}
print('De um compasso seguindo o exemplo: HH/QQQQ/XXXTXTEQH/W/HW\nW : 64, H : 32, Q : 16, E : 8, S : 4, T : 2, X : 1\nDigite 0 para finalizar.')
while True:
	
	compasso = input('\nDigite o compasso: ').split('/')
	
	if compasso == ['0']:
		break

	total = conta_duracao(compasso)
	
	print(total)
print('\nFIM DE EXECUÇÃO')	

from random import randint
print('Digite 6 numeros diferentes com valor de 1 a 99')
while True:
    teste = True
    nums_aposta = [int(x) for x in input("Numeros ").split()]
    if len(nums_aposta) != 6:
        print('Quantidade de numeros diferente do pedido')
        continue
    for i in nums_aposta:
        if not 1 <= i <= 99:
            print('Algum numero não corresponde ao intervalo [1,99]')
            teste = False
            break
        if nums_aposta.count(i) > 1:
            print('Algum numero está repetido')
            teste = False
            break
    if teste == False:
        continue
    break

nums_sorteado = [randint(1,99),randint(1,99),randint(1,99),randint(1,99),randint(1,99),randint(1,99)]

for i in nums_aposta:
    print(f'[{i:^5}]', end=' ')
print()
print('-='*25)
for i in nums_sorteado:
    print(f'[{i:^5}]', end=' ')
print()

nums_certos = 0
for i in range(6):
    if nums_aposta[i] == nums_sorteado[i]:
        nums_certos += 1

if nums_certos == 3:
    resultado = 'TERNO'
elif nums_certos == 4:
    resultado = 'QUADRA'
elif nums_certos == 5:
    resultado = 'QUINA'
elif nums_certos == 6:
    resultado = 'SENA'
else:
    resultado = 'AZAR'

print('\nResultado: ',resultado)
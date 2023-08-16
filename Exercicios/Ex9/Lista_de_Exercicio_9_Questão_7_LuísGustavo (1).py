numList = []

#Exercicio 7. Entrada.
while True:
    num = int(input("Numero escolhido: "))
    if num < 50:
        break
    print("VALOR INVALIDO! O NUMERO DEVE SER MENOR QUE 50")
    
#Exercicio 7. Entrada.
for i in range(10):
    if i == 0:
        numList.append(num)
        print(f"N[{i}] = {num}")
        continue
    else:
        num = num*2
        numList.append(num)
        print(f"N[{i}] = {num}")
        
#Exercicio 7. Saida.
print("Lista final = {}".format(numList))
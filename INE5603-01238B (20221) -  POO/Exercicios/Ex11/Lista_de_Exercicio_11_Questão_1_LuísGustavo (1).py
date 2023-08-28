import random
matriz = []
soma = 0

while True:
    ordem = int(input("Qual a ordem da Matriz? "))
    if not 12 >= ordem > 0:
        print("A ordem deve contemplar o intervalo: [0 < ordem <= 12]")
    else:
        break
while True:
    numLinha = int(input("Qual linha será analisada?")) - 1
    if numLinha > ordem or numLinha < 0:
        print("O número da linha não contempla a ordem da matriz")
    else:
        break
while True:
    operador = input("Qual a operação a ser feita? Soma [S] ou Media [M]?")
    if not operador.upper() == "S" and not operador.upper() == "M":
        print("Soma ou Media? [S/M]")
    else:
        break

for linha in range(ordem):
    col = []
    for coluna in range(ordem):
        num = round(random.uniform(-10,10),2)
        col.append(num)
    matriz.append(col)

for linha in range(0,ordem):
    for coluna in range(0,ordem):
        if linha == numLinha:
            soma += matriz[coluna][linha]
        print(f"[{matriz[coluna][linha]:^5}]", end=" ")
    print()

if operador.upper() == "S":
    print(round(soma,2))
elif operador.upper() == "M":
    print(round(soma/ordem,2))
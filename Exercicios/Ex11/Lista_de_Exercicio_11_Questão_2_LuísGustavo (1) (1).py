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
    operador = input("Qual a operação a ser feita? Soma [S] ou Media [M]?")
    if not operador.upper() == "S" and not operador.upper() == "M":
        print("Soma ou Media? [S/M]")
    else:
        break
while True:
    forma = input("Os numeros serão escolhidos manualmente [M] ou aleatoriamente [A]?")
    if forma.upper() != "M" and forma.upper() != "A":
        print("Manual ou Randomico? [M/R]")
    else:
        break
if forma.upper() == "M":
    for coluna in range(ordem):
        linhaList = []
        for linha in range(ordem):
            num = round(float(input(f"Numero na Posição [{coluna+1},{linha+1}] : ")),2)
            linhaList.append(num)
        matriz.append(linhaList)

elif forma.upper() == "A": 
    for coluna in range(ordem):
        linhaList = []
        for linha in range(ordem):
            num = round(random.uniform(-10,10),2)
            linhaList.append(num)
        matriz.append(linhaList)

for linha in range(ordem):
    for coluna in range(ordem):
        if linha > coluna:
            soma += matriz[coluna][linha]
        print(f"[{matriz[coluna][linha]:^5}]", end=" ")
    print()

if operador.upper() == "S":
    print(round(soma,2))
elif operador.upper() == "M":
    print(round(soma/ordem,2))
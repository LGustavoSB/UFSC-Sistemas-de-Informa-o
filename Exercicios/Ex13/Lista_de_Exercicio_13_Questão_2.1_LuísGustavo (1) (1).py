def escolha(resp):
    if resp.lower() == "a":
        acaoA()
    elif resp.lower() == "b":
        acaoB()
    elif resp.lower() == "c":
        acaoC()
    elif resp.lower() == "d":
        acaoD()
    elif resp.lower() == "e":
        acaoE()
    elif resp.lower() == "f":
        acaoF()
    else:
        print("Ação Inexistente")
def acaoA():
    somaPar = 0
    for i in range(ordem):
        for j in range(ordem):
            if matriz[i][j] % 2 == 0:
                somaPar += matriz[i][j]
    print(f"Soma dos Elementos Pares: {somaPar}")

def acaoB():
    soma = 0
    for i in range(ordem):
        for j in range(ordem):
            if i == j:
                soma += matriz[i][j]
    print(f"Media da Diagonal Principal: {soma/ordem}")
    
def acaoC():
    produto = 0
    matriz.reverse()
    for i in range(ordem):
        for j in range(ordem):
            if i == j:
                if produto == 0:
                    produto = matriz[i][j]
                else:
                    produto *= matriz[i][j]
    print(f"Produto da Diagonal Secundaria: {produto}")
    
def acaoD():
    soma, cont = 0, 0
    for i in range(ordem):
        for j in range(ordem):
            if i < j:
                soma += matriz[i][j]
                cont += 1
    print(f"Media dos Elementos Acima da Diagonal Principal: {soma/cont}")

def acaoE():
    soma = 0
    for i in range(ordem):
        for j in range(ordem):
            if j == ordem - 1:
                soma += matriz[i][j]
    print(f"Soma dos Elementos da Ultima Coluna: {soma}")

def acaoF():
    menorValor = -1
    for i in range(ordem):
        for j in range(ordem):
            if i == 0:
                if menorValor == -1:
                    menorValor = matriz[i][j]
                elif menorValor > matriz[i][j]:
                    menorValor = matriz[i][j]
    print(f"Menor Valor da Primeira Linha: {menorValor}")


ordem = int(input("Qual a ordem da matriz? "))
matriz = []
print("Digite o numero de cada posição da matriz, em um intervalo de [0,100]")

for i in range(ordem):
    linhaMatriz = []
    for j in range(ordem):
        while True:
            num = int(input(f"[{i},{j}]: "))
            if not 0 <= num <= 100:
                print("Numero fora do intervalo")
                continue
            break
        linhaMatriz.append(num)
    matriz.append(linhaMatriz)  
print("Matriz Formada:")
for i in range(ordem):
    for j in range(ordem):
            print(f"[{matriz[i][j]:^5}]", end=" ")
    print()
    
print("\nO que voce deseja dessa matriz?\na) Soma dos elementos pares\nb) Média da diagonal principal\nc) Produto da diagonal secundária\nd) Média dos elementos acima da diagonal principal\ne) Soma dos elementos da ultima coluna\nf) Menor valor da primeira linha")
while True:
    escolha(input("Ação: "))
    
    parada = input("\nDeseja tomar outra ação? [S/N]: ")
    if parada.upper() == "N":
        break
print("\nFIM DE EXECUÇÃO\n")
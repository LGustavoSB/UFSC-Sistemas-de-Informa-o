from random import randint

numList = []
numMinasList = []

#Exercicio 8. Entrada Inicial (Decisão da forma de escolha das posições e do tamanho do tabuleiro)
resp = input("Digite 1 se você deseja escolher as posições das minas\nDigite 2 se quiser que elas sejam selecionadas aleatoriamente\n")
numTestes = int(input("Quantas células tem o tabuleiro? "))

#Exercicio 8. Formadores da Lista
if resp == "1":
    for i in range(numTestes):
        numList.append(int(input("Diga se há uma mina no espaço (1) ou não (0). [0/1]")))
        
elif resp == "2":
    for i in range(numTestes):
        numList.append(randint(0,1))
        
#Exercicio 8. Teste de Posição das Minas
aux = len(numList) - 1
for i in range(len(numList)):
    numMinas = 0
    if i == 0:
        if numList[0] == 1:
            numMinas += 1
        if numList[1] == 1:
            numMinas +=1
    elif i == aux:
        if numList[aux] == 1:
            numMinas += 1
        if numList[aux - 1] == 1:
            numMinas += 1        
    elif numList[i] == 1:
        numMinas += 1
        if numList[i-1] == 1:
            numMinas += 1
        if numList[i+1] == 1:
            numMinas += 1
    elif numList[i] == 0:
        if numList[i-1] == 1:
            numMinas += 1
        if numList[i+1] == 1:
            numMinas += 1          
    numMinasList.append(numMinas)
    
#Exercicio 8. Saídas
print("Posições das minas no tabuleiro: ",numList)
print("Numeros de minas proximas a elas:",numMinasList)
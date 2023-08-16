#QUESTÃO 1

#Função Questão 1. a).
def calcNove(numList_A):
    numNove = str(numList).count("9")
    if numNove > 0:
        return (f"Existem {numNove} numeros 9 na tupla")
    else:
        print("Não há nenhum número 9 na tupla")

#Função Questão 1. b).
def calcTres(numList_B):
    for i in range(5):
        if numList_B[i] == 3:
            respTres = (f"O primeiro número 3 da tupla está na posição {i+1}")
            break
    if numList.count(3) == 0:
        respTres = ("Não há nenhum número com valor 3 na tupla")
    return respTres

#Função Questão 1. c).
def calcPar(numList_C): 
    numPar = []
    for i in range(5):
        if numList_C[i] % 2 == 0:
            if numPar == []:
                numPar = [numList_C[i]]
            elif numPar != []:
                numPar.append(numList_C[i])
    if numPar != []:
        respPar = (f"Os números pares são {numPar}")
    else:
        respPar = ("Não existem números pares na tupla")
    return respPar

#Questão 1. Entrada.
print("Digite numeros para integrar sua tupla: ")
numList = (int(input("Numero 1: ")),
            int(input("Numero 2: ")),
            int(input("Numero 3: ")),
            int(input("Numero 4: ")),
            int(input("Numero 5: ")))
print(f"Observando a tupla {numList}, podemos analisar que:")

#Questão 1. a).
print(calcNove(numList))

#Questão 1. b).
print(calcTres(numList))
    
#Questão 1. c).
print(calcPar(numList))

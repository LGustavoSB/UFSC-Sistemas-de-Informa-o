from random import randint

#Funçao Questão 2.
def calcNum(nums):
    maiorNum, menorNum = 0, 0
    for i in range(len(numList)):
        var = numList[i]
        if maiorNum == 0:
            maiorNum = var
        elif maiorNum < var:
            maiorNum = var
        if menorNum == 0:
            menorNum = var
        elif menorNum > var:
            menorNum = var
    return maiorNum, menorNum

#Questão 2. Entrada.
numList = (randint(0,10),
           randint(0,10),
           randint(0,10),
           randint(0,10),
           randint(0,10))

#Questão 2. Saída.
print(f"Da tupla {numList}: ")
print("O maior numero é {}, enquanto o menor é {}".format((calcNum(numList)[0]), (calcNum(numList)[1])))      

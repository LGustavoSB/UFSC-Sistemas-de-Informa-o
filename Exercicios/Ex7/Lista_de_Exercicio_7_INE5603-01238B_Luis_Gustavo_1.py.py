"""
EX 1 - 1437
drc = 0
n = int(input("Quantidade de comandos: "))
while 1 > n or n > 1000:
    print("A quantidade de comandos deve ser no minimo 1 e no maximo 1000")
    n = int(input("Quantidade de comandos: "))
cmnds = input("Diga a direção (E para Esquerda e D para Direita): ")
while len(cmnds) != n:
    print("Quantidade de comandos diferente do informado")
    cmnds = input("Diga a direção (E para esquerda e D para direita): ")
drt = cmnds.count("D")
esqrd = cmnds.count("E")
if drt > 0:
    for i in range(0,drt):
        drc += 90
        if drc == 360:
            drc = 0
if esqrd > 0:
    for i in range(0,esqrd):
        drc -= 90
        if drc == -360:
            drc = 0
if drc == 0 or drc == 360 or drc == -360:
    print("N")
elif drc == 90 or drc == -90:
    print("L")
elif drc == 180 or drc == -180:
    print("S")
elif drc == 270 or drc == -270:
    print("O")
"""

extraTrabalho, extraCasa, gc_casa, gc_trabalho = 0, 0, 0, 0
numDias = int(input("Numero de dias previstos: "))
while 1 > numDias or numDias > 1000:
    print("A quantidade de dias deve ser no minimo 1 e no maximo 1000")
    numDias = int(input("Numero de dias previstos: "))
print("Digite -sol- se não chover e -chuva- se chover")
for i in range(numDias):
    prvsIda, prvsVolta = list(input("Digite primeiro a previsao na ida e depois na volta: ").split())
    if prvsIda == "chuva" and extraCasa == 0:
        gc_casa += 1
        extraTrabalho += 1
    elif prvsIda == "chuva" and extraCasa > 0:
        extraCasa -= 1
        extraTrabalho += 1        
    if prvsVolta == "chuva" and extraTrabalho == 0:
        gc_trabalho += 1
        extraCasa += 1
    elif prvsVolta == "chuva" and extraTrabalho > 0:
        extraTrabalho -= 1
        extraCasa += 1
print(f"Voce deve deixar {gc_casa} guarda-chuvas em casa e {gc_trabalho} no trabalho")

"""
EX 3 = 1192
def calcPaula(numPaula):
    if numPaula[0] == numPaula[2]:
        return(int(numPaula[2]) * int(numPaula[0]))
    elif numPaula[1] == numPaula[1].upper():
        return(int(numPaula[2]) - int(numPaula[0]))
    elif numPaula[1] == numPaula[1].lower():
        return(int(numPaula[2]) + int(numPaula[0]))

numTestes = int(input("Numero de testes: "))
for i in range(numTestes):
    num = str(input("Digite um conjunto de 3 caracteres onde o primeiro e o ultimo devem ser números de 0 a 9, e o segundo uma letra, maiuscula ou minuscula:\n"))
    while(len(num) != 3 or 9 < int(num[0]) < 0 or 9 < int(num[2]) < 0):
        print("As instruções não foram seguidas!")
        num = str(input("Tente Novamente: "))
    print(f"{calcPaula(num)}")
"""
"""
EX 4 - 1168
def calcLeds(numLeds, i):
    if(numLeds[i] == "0"):
        return 6
    if(numLeds[i] == "1"):
        return 2
    elif(numLeds[i] == "2"):
        return 5
    elif(numLeds[i] == "3"):
        return 5
    elif(numLeds[i] == "4"):
        return 4
    elif(numLeds[i] == "5"):
        return 5
    elif(numLeds[i] == "6"):
        return 6
    elif(numLeds[i] == "7"):
        return 3
    elif(numLeds[i] == "8"):
        return 7
    elif(numLeds[i] == "9"):
        return 6
    else:
        return 0
soma = 0
numTestes = int(input("Numero de testes: "))
for i in range(numTestes):
    num = int(input("Qual será o número mostrado? "))
    while num > 10**100 or num < 0:
        print("Escolha um numero entre 1 e 10^100")
        num = input("Qual será o número mostrado? ")
    for i in range(len(str(num))):
        soma += calcLeds(str(num), i)
    print(f"{soma} leds")
    soma = 0
"""
"""
EX 5 - 1094
coelhos, ratos, sapos = 0, 0, 0
numTestes = int(input("Numero de testes: "))
print("C: Coelho\nR: Rato\nS: Sapos")
for i in range(numTestes):
    qtdCobaia = input("Diga o número de cobaias e de que tipo são no formato N T, onde N é o numero e T o tipo: ")
    qtd = int(qtdCobaia[0: len(qtdCobaia) - 2])
    while qtd > 15 or qtd < 1:
        print("Entrada inválida!")
        qtdCobaia = input("Tente Novamente!")
    if qtdCobaia[len(qtdCobaia) - 1].upper() == "C":
        coelhos += qtd
    elif qtdCobaia[len(qtdCobaia) - 1].upper() == "R":
        ratos += qtd
    elif qtdCobaia[len(qtdCobaia) - 1].upper() == "S":
        sapos += qtd
    else:
        print("Valor inválido")
total = coelhos + sapos + ratos
perCoelhos = (coelhos/total)*100
perRatos = (ratos/total)*100
perSapos = (sapos/total)*100
print(f"Total de cobaias: {total}\nQuantidade de Coelhos: {coelhos}\nQuantidade de Ratos: {ratos}\nQuantidade de Sapos: {sapos}")
print("Percentual de coelhos: {:.2f}\nPercentual de ratos: {:.2f}\nPercentual de sapos: {:.2f}".format(perCoelhos, perRatos, perSapos))
"""
"""
EX 6
barra = "-"*50
resp = "SIM"
while resp.upper() == "SIM":
    num = input("Digite um numero e descubra se é divisivel por 3: \n")
    while 1 > int(num) or int(num) > 10**9:
        print("Valor inválido, ou o número é muito alto, ou é menor que 1")
        num = input("Tente novamente! ")
    soma = 0
    for i in range(len(num)):
        soma += int(num[i])
    if soma % 3 == 0:
        print(f"É divisivel por 3\n{barra}")
    else:
        print(f"Não é divisivel por 3\n{barra}")
    resp = input("Quer testar outro número? Em caso afirmativo, digite SIM: ")
print(f"{barra}\nFim")
"""
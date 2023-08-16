#Questão 3. Função.
def calcNumRptd(qtdNum):
    numRptd = []
    numList = []
    cont = 0
    for i in range(qtdNum):
        numList.append(int(input(f"Numero {i+1}: ")))
        num = str(numList)
        if num.count(str(numList[i])) > 1:
            cont += 1
            numRptd.append(numList[i])
    if cont > 0:
        resp = f"Existem números repetidos\nEstes numeros foram {numRptd}"
    if cont == 0:
        resp = "Não há nenhum número repetido"
    return resp

#Questão 3. Entrada.
rptdList = calcNumRptd(int(input("Quantos números serão adicionados a lista? ")))
   
#Questão 3. Saida.        
print(rptdList)
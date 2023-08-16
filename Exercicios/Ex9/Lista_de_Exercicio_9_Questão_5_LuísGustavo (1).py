#Questão 5. Função.
def testPlugs():
    for i in range(5):
        if conector1[i] == conector2[i]:
            resp = "N"
        else:
            resp = "S"
    return resp

#Questão 5. Entrada.
print("Demonstre os pontos de conexão no formato (n n n n n n)\nOnde n pode ser 0 para saída e 1 para entrada")
conector1 = list(input("Digite os pontos de conexão do primeiro conector: ").split(" "))
conector2 = list(input("Digite os pontos de conexão do segundo conector: ").split(" "))

#Questão 5. Saída.
print(testPlugs())
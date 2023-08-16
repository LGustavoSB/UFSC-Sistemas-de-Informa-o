def validaNum(qtdNumeros):
    while True:
        if not 1 <= qtdNumeros <= 1000:
            print("Quantidade Inválida, tente ficar no intervalo de 1 a 1000 numeros")
            qtdNumeros = int(input("Quantos números serão colocados na lista? "))
            continue
        break
    return qtdNumeros


def multiploDois():
    contDois = 0
    for i in listaNumeros:
        if i % 2 == 0:
           contDois += 1
    return contDois


def multiploTres():
    contTres = 0
    for i in listaNumeros:
        if i % 3 == 0:
            contTres += 1
    return contTres


def multiploQuatro():
    contQuatro = 0
    for i in listaNumeros:
        if i % 4 == 0:
            contQuatro += 1
    return contQuatro  


def multiploCinco():
    contCinco = 0
    for i in listaNumeros:
        if i % 5 == 0:
            contCinco += 1
    return contCinco


listaNumeros = []
qtdNumeros = validaNum(int(input("Quantos números serão colocados na lista? ")))
print("\nDigite os numeros escolhidos para a lista:")
for i in range(qtdNumeros):
    listaNumeros.append(int(input(f"Nº{i+1}: ")))
print(f"{multiploDois()} Multiplo(s) de 2\n{multiploTres()} Multiplo(s) de 3\n{multiploQuatro()} Multiplo(s) de 4\n{multiploCinco()} Multiplo(s) de 5")
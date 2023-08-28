def validaNumSuspeitos(qtdSuspeitos):
    if not 2 <= qtdSuspeitos <= 1000:
        print("Numero Invalido, o numero de suspeitos deve ser de 2 a 1000 suspeitos")
        while True:
            qtdSuspeitos = int(input("Quantos suspeitos? "))
            if not 2 <= qtdSuspeitos <= 1000:
                continue
            break


while True:
    listaSuspeitos = []

    numSuspeitos = int(input("Quantos suspeitos? "))
    
    if numSuspeitos == 0:
        break
    
    validaNumSuspeitos(numSuspeitos)
        
    for i in range(numSuspeitos):
        listaSuspeitos.append(int(input(f"De 1 a {10**4}, quão suspeito é o Suspeito Nº{i+1}? ")))
    
    culpado = listaSuspeitos.index((((sorted(listaSuspeitos))[::-1])[1]))
    
    print(f"\nO culpado é o Suspeito Nº{culpado+1}\n")

print("\nFIM DE EXECUÇÃO")
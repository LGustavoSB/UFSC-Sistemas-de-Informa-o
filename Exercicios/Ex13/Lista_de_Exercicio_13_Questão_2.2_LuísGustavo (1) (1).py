from random import randint 
b = "-"*25
print(f"{b}\n    JOGO DA MEGA SENA\n{b}")
numJogos = int(input("Quantos jogos você quer que eu sorteie? "))
for i in range(numJogos):
    numSorteados = []
    for j in range(6):
        numSorteados.append(randint(1,60))
    print(f"Jogo {i+1}: {numSorteados}")
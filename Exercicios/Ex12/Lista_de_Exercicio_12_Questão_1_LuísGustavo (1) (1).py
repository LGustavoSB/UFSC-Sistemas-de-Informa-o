import random
voluntList = []
sobrevList = []
while True:
    numVolunt = int(input("Quantos voluntarios mergulharam? "))
    if 1 <= numVolunt <= 10**4:
        break
    print("O numero de voluntarios deve estar entre 1 e 10000")
while True:
    numSobrev = int(input("Quantos retornaram? "))
    if numSobrev < 1:
        print("Deve haver pelo menos um sobrevivente")
    elif numSobrev > numVolunt:
        print("O numero de sobreviventes não pode ser maior que o de voluntários")
    else:
        break
for i in range(1, numVolunt + 1):
    voluntList.append(i)
sobrev = (random.sample(voluntList, k = numSobrev))
print("Os sobreviventes foram:", sorted(sobrev))
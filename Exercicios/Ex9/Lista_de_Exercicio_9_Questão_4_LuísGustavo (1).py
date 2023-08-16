numProx = 101
numTestes = int(input("Quantos sorteios serão feitos? "))
for i in range(numTestes):
    numProx = 100
    numList = []
    numAlunos, numSort = input("Diga o número de alunos participando do sorteio e o número a ser adivinhado: ").split()
    numAlunos = int(numAlunos)
    numSort = int(numSort)
    while numAlunos > 10 or numAlunos < 4 or numSort > 100 or numSort < 1:
        if numAlunos > 10 or numAlunos < 4:
            print("O número de alunos participando deve estar no intervalo de 4 <= Alunos <= 10")
            numAlunos = int(input("Quantos alunos participarão? "))
        if numSort > 100 or numSort < 1:
            print("O número sorteado deve estar no intervalo de 1 <= N <= 100")
            numSort = int(input("Qual numero escolhido"))
    numList = input("Numeros escolhidos: ").split(" ")
    while len(numList) != numAlunos:
        print("Quantidade de numeros diferente da de alunos")
        numList = input("Numeros escolhidos: ").split(",")
    for c in range(numAlunos):
        if int(numList[c]) >= numSort:
            dif = int(numList[c]) - numSort
        elif int(numList[c]) <= numSort:
            dif = numSort - int(numList[c])
        if dif < numProx:
            numProx = dif
            alunoGanhador = c+1
            numGanhador = numList[c]
    print(f"Sorteio {i+1}:\nNumero Sorteado: {numSort}\nVencedor: Aluno {alunoGanhador}\nNumero Escolhido Pelo Aluno: {numGanhador} ")
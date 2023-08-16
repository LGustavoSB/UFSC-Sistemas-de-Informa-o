def testeNota(): #Verifica as notas
    '''Valida as notas'''
    while True:
        notaAluno = float(input(f"Nota {i+1}: "))
        if not 0 <= notaAluno <= 10:
            print("Nota Inválida, Tente Novamente")
            continue
        break    
    return notaAluno


def testeEscolha():
    '''Valida a escolha'''
    while True:
        escolha = input("\nDeseja consultar as notas de algum aluno? [S/N]: ")
        if escolha.upper() != "S" and escolha.upper() != "N":
            print("Opção Inválida")
            continue
        break
    return escolha


def alunoBoletim():
    '''Busca as notas pelo nome do aluno e verifica se ele está cadastrado'''
    cont = 0
    for i in range(numAlunos):
        if nomeAluno.upper() == listaAlunos[i][0].upper():
            print(f"\nAluno: [{listaAlunos[i][0]}]\nNotas: {listaAlunos[i][1:4]}")
        else:
            cont += 1
        if cont == numAlunos:
            print("\nALUNO NÃO IDENTIFICADO")
            continue
        
        
listaAlunos = []

numAlunos = int(input("\nQual o número de alunos? "))
if numAlunos <= 0:
    print("Nenhum aluno foi cadastrado")
else:
    print("Digite o nome dos alunos e 3 notas, de 0 a 10\n")

    for i in range(numAlunos):
        soma = 0
        aluno = []
        
        aluno.append(input("Qual o nome do aluno? "))
        
        for i in range(3):
            notaAluno = testeNota()
            aluno.append(notaAluno)  
            soma += notaAluno
        aluno.append(round(soma/3,2))
        listaAlunos.append(aluno)
    print()    
    for i in range(numAlunos):
        print(f"Aluno: [{listaAlunos[i][0]}]\nMedia Final: [{listaAlunos[i][4]}]")
        
    while True:
        escolha = testeEscolha()
        
        if escolha.upper() != "S":
            break
        
        nomeAluno = input("De qual aluno? ")
        alunoBoletim()
        
print("\nFIM DE EXECUÇÃO")
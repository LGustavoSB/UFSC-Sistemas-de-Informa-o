alunoFut = list()
alunoNat = list()
alunoBas = list()
alunoVol = list()
alunoTotal = list()
descontAlunos = list()

while True:
    esporte = input("Diga qual esporte haverá adição de alunos: ")
    aluno = input("Qual o nome do aluno a ser cadastrado? ")
    alunoTotal.append(aluno)
    if esporte.upper().strip() == "FUTEBOL":
        alunoFut.append(aluno)
    elif esporte.upper().strip() == "BASQUETE":
        alunoBas.append(aluno)
    elif esporte.upper().strip() == "NATAÇÃO":
        alunoNat.append(aluno)
    elif esporte.upper().strip() == "VOLEI":
        alunoVol.append(aluno)
    relAlunos = set(alunoTotal)
    resp = str(input("Gostaria de inscrever mais alunos? [S/N]: "))
    while resp.upper() != "S" and resp.upper() != "N":
        resp = input("[S/N]: ")
    if resp.upper() == "N":
        break
for i in range(len(alunoTotal)):
    if alunoTotal.count(alunoTotal[i]) >= 2:
        descontAlunos.append(alunoTotal[i])
        
print(f"Os alunos cadastrados por modalidade:\nFutebol: {alunoFut}\nBasquete: {alunoBas}\nNatação: {alunoNat}\nVolei: {alunoVol}")
print(f"Total de Alunos: {len(relAlunos)}\nAlunos no Futebol: {len(alunoFut)}\nAlunos no Basquete: {len(alunoBas)}\nAlunos na Natação: {len(alunoNat)}\nAlunos no Volei: {len(alunoVol)}")
print(f"Os alunos {set(descontAlunos)} receberam desconto por estarem inscritos em mais de uma modalidade")
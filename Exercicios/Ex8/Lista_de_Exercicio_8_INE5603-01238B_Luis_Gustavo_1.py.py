"""
EX 1
maior_nota, menor_nota, soma = 0, 10, 0
notas = list()
for i in range(3):
    notas.append(float(input(f"Digite a nota {i+1} do aluno: ")))
    while notas[i] < 0 or notas[i] > 10:
        del notas[i]
        print("A nota deve estar entre 0 e 10")
        notas.append(float(input(f"Digite a nota {i+1} do aluno: ")))
    if notas[i] > maior_nota:
        maior_nota = notas[i]
    if notas[i] < menor_nota:
        menor_nota = notas[i]
    soma += notas[i]
media = soma/3
compara_nota = maior_nota - menor_nota
print("A menor nota foi: {:.2f}\nA maior nota foi: {:.2f}\nA média das notas foi: {:.2f}\nA diferença entre a maior e a menor nota foi: {:.2f}".format(menor_nota, maior_nota, media, compara_nota))
"""
"""
EX 2
cont, num_rptd = 0, 0
num_testes = int(input("Quantos elementos serão inseridos?"))
nums_list = list()
num_rptd = list()
for i in range(num_testes):
    nums_list.append(int(input("Digite um número inteiro: ")))
    num = str(nums_list)
    if num.count(str(nums_list[i])) > 1:
        cont += 1
        num_rptd.append(nums_list[i])
if cont > 0:
    print("Existem números repetidos")
    print(f"Estes numeros foram {num_rptd}")
if cont == 0:
    print("Não há nenhum número repetido")
"""
"""
EX 3
maior_num, menor_num = 0, 10
lista = (3, 9, 2, 4, 6, 1, 7, 8, 5)
num_lista = lista
for i in range(len(lista)):
    if num_lista[i] > maior_num:
        maior_num = num_lista[i]
        pos_maior = i + 1
    if num_lista[i] < menor_num:
        menor_num = num_lista[i]
        pos_menor = i + 1
print(f"O menor numero é {menor_num} e está na posição: {pos_menor}")
print(f"O maior numero é {maior_num} e está na posição: {pos_maior}")
"""
"""
EX 4
num_tests = int(input("Quantos elementos serão inseridos? "))
multplc_list = list()
final = list()
num = int(input("Digite o numero a ser multiplicado: "))
for i in range(num_tests):
    multplc_list.append(int(input("Digite um multiplicador: ")))
    final.append(multplc_list[i]*num)
print(f"O numero {num} multiplicado pelos numeros {multplc_list} tem como resultado {final}, respectivamente")
"""
"""
EX 5
num_list = list(range(21))
print("Seleção automatica de 0 a 20")
resp = input("Deseja criar a propria listagem? Em caso afirmativo, digite SIM: ")
if resp.upper() == "SIM":
    print("Digite 20 números para integrar a lista")
    num_list = []
    for i in range(20):
        num = input(f"Número {i+1}: ")
        num_list.append(num)   
print(f"Lista Normal:\n{num_list[0:21]}")
num_list_final = num_list[21:0:-1]
num_list_final.append(num_list[0])
print(f"Lista Invertida:\n{num_list_final}")
"""
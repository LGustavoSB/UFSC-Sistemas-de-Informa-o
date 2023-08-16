"""
EX 1.1
for i in range (2004, 2097, 4):
    print(i)
"""
'''
EX 1.2
for i in range (2096, 2003, -4):
    print(i)
'''
'''
EX 1.3
c = int(input("Data inicial "))
f = int(input("Data final "))
o = int(input("A ordem "))
for i in range (c, f, o):
    print(i)
'''
"""
EX 2
for i in range (1, 51):
    if ((i % 2) != 0):
        print(i)
"""
"""
EX 3
for i in range (5):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    mensalidade = float(input("Mensalidade do aluno: "))
    
    if i == 0:
        notaMaior = nota
        nomeMaior = nome
        mensalidadeMaior = mensalidade
    elif nota > notaMaior:
        notaMaior = nota
        nomeMaior = nome
        mensalidadeMaior = mensalidade
mensalidadeFinal = mensalidadeMaior * 0.70
print(f"O aluno {nomeMaior} terá um desconto em sua mensalidade, mudando de {mensalidadeMaior} para {mensalidadeFinal} ")
"""
"""
EX 4
par = 0
impar = 0
for i in range (10):
    n = int(input("Digite um número inteiro "))
    if ((n % 2) != 0):
        impar = impar + 1
    else:
        par = par + 1
print(f"{par} são par e {impar} são ímpar")
"""
"""
EX 5
num = int(input("Digite um número inteiro "))
div = 0

for i in range (num, 0, -1):
    if (num % i) == 0:
        div = div + 1
if (div == 2):
    print("É primo")
else:
    print("Não é primo")
"""
"""
EX 6
num = int(input("Digite um número inteiro "))
div = 0
cont = 0
for i in range (num, 0, -1):
    if (num % i) == 0:
        cont = cont + 1
if (cont == 2):
    print("É primo")
else:
    print("Não é primo")
    for i in range (num, 0, -1):
        if (num % i) == 0:
            print(i)
"""        
"""
EX 7
pJ = 0
pA = 0
pI = 0
n = int(input("Número de pessoas "))
for i in range (0, n):
    idade = int(input("Qual sua idade?"))
    if 0 < idade < 25:
        pJ = pJ + 1
    elif 26 < idade < 60:
        pA = pA + 1
    elif idade > 60:
        pI = pI + 1
if pJ > pI and pJ > pA:
    print("A turma é jovem")
elif pA > pJ and pA > pI:
    print("A turma é adulta")
elif pI > pJ and pI > pA:
    print("A turma é idosa")    
"""
"""
EX 8
soma = 0
num1 = int(input("Número inicial: "))
num2 = int(input("Número final: "))
for i in range (num1, num2+1):
    print(i)
    soma = soma + i
print(f"A soma dos números inteiros entre {num1} e {num2} é {soma}")
"""
"""
EX 9
num = int(input("Digite um número "))
for i in range (11):
    mult = num * i
    print(f"{num} x {i} = {mult}")
"""
"""
EX 10
n = int(input("Quantos números devem ser lidos? "))
for i in range (0, n):
    num = int(input("Digite um número "))
    if i == 0:
        numMaior = num
        numMenor = num
    elif num > numMaior:
        numMaior = num
    elif num < numMenor:
        numMenor = num

print(f"O o maior número é {numMaior} e o menor é {numMenor}")
"""


"""
EX 12
dist1 = 0
nDist = 0
praias = int(input("Digite quantas praias devem ser cadastradas "))
for i in range (0, praias):
    nome = input("Diga o nome da praia ")
    dist = int(input("Indique a distancia da praia do centro da cidade "))
    if i == 0:
        maisLonge = nome
        distMaior = dist
    elif dist > distMaior:
        maisLonge = nome
        distMaior = dist
    if 15 <= dist <= 20:
        nDist = 1 + i

    
print(f"{maisLonge} é a praia mais distante")
print(f"{nDist} praia(s) estão entre 15 e 20km do centro")
"""

"""
Não consegui fazer a média na 10 e 12. Não fiz a 11.
"""
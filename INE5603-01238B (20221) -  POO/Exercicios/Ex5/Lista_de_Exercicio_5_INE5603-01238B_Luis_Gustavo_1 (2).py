"""
EX 1

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
if num1 > num2:
    print("Decrescente")
    
else:
    print("Crescente")
"""
"""
EX 2
n = int(input("Quantidade de testes"))
cont = 0
soma = 0
while cont != n:
    soma = 0
    num1 = int(input(": "))
    num2 = int(input(": "))
    if num1 < num2:
        num1 += 1
        for i in range(num1, num2):
            if i % 2 != 0:
                soma += i
    else:
        num2 += 1
        for i in range(num2, num1):
            if i % 2 != 0:
                soma += i
    print(soma)
    cont += 1
"""

"""
EX 3
val = float(input("Digite um valor: "))
n = val // 100
print("NOTAS:\n",n,"nota(s) de R$ 100.00" )
resto = val % 100
n = resto // 50
print(n,"nota(s) de R$ 50.00" )
resto = resto % 50
n = resto // 20
print(n,"nota(s) de R$ 20.00" )
resto = resto % 20
n = resto // 10
print(n,"nota(s) de R$ 10.00" )
resto = resto % 10
n = resto // 5
print(n,"nota(s) de R$ 5.00" )
resto = resto % 5
n = resto // 2
print(n,"nota(s) de R$ 2.00" )
resto = resto % 2
n = resto // 1
print("MOEDAS:\n",n,"moeda(s) de R$ 1.00" )
resto = resto % 1
n = resto // 0.50
print(n,"moeda(s) de R$ 0.50" )
resto = resto % 0.50
n = resto // 0.25
print(n,"moeda(s) de R$ 0.25" )
resto = resto % 0.25
n = resto // 0.10
print(n,"moeda(s) de R$ 0.10" )
resto = resto % 0.10
n = resto // 0.05
print(n,"moeda(s) de R$ 0.05" )
resto = resto % 0.05
n = resto // 0.01
print(n,"moeda(s) de R$ 0.01" )
resto = resto % 0.01
"""
'''
EX 4
d, vF, vG = input("Digite a distancia entre os botes, a velocidade do fugitivo e a velocidade da guarda: ").split()
d = int(d)
vF = int(vF)
vG = int(vG)
dist = ((12**2)+(d**2))**0.5
tF = 12/vF
tG = dist/vG
if tF > tG:
    print("S")
else:
    print("N")
'''
"""
EX 5
p1 = int(input("Tempo do primeiro: "))
u1 = int(input("Tempo do ultimo: "))
while p1 > u1:
    print("OOPS, o Primeiro lugar deve ter um tempo menor q1ue o último, TENTE NOVAMENTE: ")
    p1 = int(input("Tempo do primeiro: "))
    u1 = int(input("Tempo do ultimo: "))
p2, u2 = 0, 0
dif = u1 - p1
volta = 1
while dif < p1:
    p2 += p1
    u2 += u1
    dif = u2 - p2
    volta += 1
print(volta)
"""
"""
EX 6
import math
notaMaior = 0
notaMenor = 10
media = 0
for i in range(5):
    nota = float(input("Digite uma nota de 5 a 10 "))
    while 10 < nota or nota < 5:
        nota = float(input("OOOPS, TENTE NOVAMENTE\nDigite uma nota de 5 a 10 "))
    if nota > notaMaior:
        notaMaior = nota
    if nota < notaMenor:
        notaMenor = nota
    media += nota
media = media - notaMaior - notaMenor
print(round(media,2))
"""
'''
EX7
resp = "SIM"
cont = 1
t1, t2 = 0, 0
while resp == "SIM":
    print("TESTE", cont)
    nD = int(input("Quantos depósitos serão feitos? "))
    for i in range(nD):
        v1 = int(input("Valor colocado no primeiro cofre: "))
        v2 = int(input("Valor colocado no segundo cofre: "))
        t1 += v1
        t2 += v2
        dif = t1 - t2
        print(dif)
    resp = input("Quer fazer mais depósitos? Digite SIM ou NAO: ")
    while resp != "NAO" and resp != "SIM":
        print("RESPOSTA INVÁLIDA")
        resp = input("Quer fazer mais depósitos? Digite SIM ou NAO: ")
    if resp == "SIM":
        nD = int(input("Quantos depósitos? "))
        cont += 1
    if resp == 'NAO':
        print("FIM")
'''
"""
EX 8
cont = 1
n = int(input("Quantos testes serão feitos? "))
for i in range(n):
    print("TESTE", cont)
    val = int(input("Digite o valor: "))
    n50 = val // 50
    val = val % 50
    n10 = val // 10
    val = val % 10
    n5 = val // 5
    val = val % 5
    n1 = val // 1
    val = val % 1
    cont += 1
    print(n50, n10, n5, n1, "\n")
"""
"""
EX 10
cont = 0

n = int(input("Quantos testes serão feitos? "))
while n != cont:
    d = int(input("Quantas dobras no papel: "))
    cont += 1
    nq = (1+2**d)*(1+2**d)
    print(f"Teste {cont}")
    print(f"{nq}\n")

"""
"""
EX 11
cont = 1
x = int(input("Digite um número para X: "))
z = int(input("Digite outro número, agora para Z: "))
soma = x
while z <= x:
    print("OOOPS, Z deve ser maior que X")
    z = int(input("Digite outro número: "))
while soma <= z:
    x += 1
    cont += 1
    soma += x
print(cont)
"""
"""
EX 12
x = int(input("Coordenada X em que a bola caiu: "))
y = int(input("Coordenada Y em que a bola caiu: "))
if x >= 0 and x <= 432 and y >= 0 and y <= 468:
    print("Dentro")
else:
    print("Fora")
"""
'''
EX 13
p = int(input("Escolha a posição de P entre 0 ou 1: "))
r = int(input("Escolha a posição de R entre 0 ou 1: "))
while p != 1 and p != 0 or r != 1 and r != 0:
    print("ESCOLHA 0 OU 1")
    p = input("Escolha a posição de P: ")
    r = input("Escolha a posição de R: ")
if p == 0:
    print("C")
elif p == 1 and r == 0:
    print("B")
elif p == 1 and r == 1:
    print("A")
'''
"""
EX 14
q = 0
n = int(input("Quantas bandejas o garçom entregou? "))
for i in range (n):
    l = int(input("Quantas latas foram levadas em cada bandeja? "))
    c = int(input("E quantos copos? "))
    if l > c:
        q += c
print(f"Foram quebrados {q} copos")
"""
"""
EX 16
pg = float(input("Qual o preço do litro da gasolina? ")) 
pa = float(input("Qual o preço do litro do alcool? ")) 
rg = float(input("Quantos KM por litro faz com gasolina? ")) 
ra = float(input("Quantos KM por litro faz com alcool? "))
g = pg / rg
a = pa / ra
if g >= a:
    print("G")
else:
    print("A")
"""
"""
EX 17
cont1, cont2 = 0, 0
resp = input("Deseja jogar Pedra Papel Tesoura? Digite SIM ou NAO ")
while resp == "SIM":
    print("Digite 1 (PEDRA), 2 (PAPEL) ou 3 (TESOURA)")
    j1 = int(input("Escolha do jogador 1: "))
    j2 = int(input("Escolha do jogador 2: "))
    while j1 != 1 and j1 != 2 and j1 != 3 or j2 != 1 and j2 != 2 and j2 != 3:
        print("RESPOSTA INVÁLIDA\nDigite 1 (PEDRA), 2 (PAPEL) ou 3 (TESOURA)")
        j1 = int(input("Escolha do jogador 1: "))
        j2 = int(input("Escolha do jogador 2: "))
    if j1 == 1 and j2 == 2 or j1 == 3 and j2 == 1 or j1 == 2 and j2 == 3:
        print("Jogador 2 venceu")
        cont2 += 1
    elif j1 == 2 and j2 == 1 or j1 == 1 and j2 == 3 or j1 == 3 and j2 == 2:
        print("Jogador 1 venceu")
        cont1 += 1
    resp = input("Deseja continuar jogando? Digite SIM ou NAO ")
    while resp != "SIM" and resp != "NAO":
        resp = input("RESPOSTA INVÁLIDA\nDeseja continuar jogando? Digite SIM ou NAO ")
print(f"Jogo encerrado\nO placar ficou Jogador1  {cont1} X {cont2}  Jogador2")
"""
"""
EX 18
n1 = int(input("Digite um número "))
n2 = int(input("Digite outro número "))
n3 = int(input("Digite mais um número "))
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print(n3, n2, n1)
    elif n3 > n2:
        print(n2, n3, n1)
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print(n3, n1, n2)
    elif n3 > n1:
        print(n1, n3, n2)
if n3 > n2 and n3 > n1:
    if n1 > n2:
        print(n2, n1, n3)
    elif n2 > n1:
        print(n1, n2, n3)
"""
"""
EX 19
l1 = float(input("Diga o tamanho do lado A do triangulo "))
l2 = float(input("Diga o tamanho do lado B do triangulo "))
l3 = float(input("Diga o tamanho do lado C do triangulo "))
while l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
    print("ISSO NÃO É UM TRIÂNGULO (Ex: A + B > C )")
    l1 = float(input("Diga o tamanho do lado A do triangulo "))
    l2 = float(input("Diga o tamanho do lado B do triangulo "))
    l3 = float(input("Diga o tamanho do lado C do triangulo "))
if l1 == l2 and l2 == l3:
    print("Triangulo Equilatero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Triangulo Isósceles")
else:
    print("Triangulo Escaleno")
"""
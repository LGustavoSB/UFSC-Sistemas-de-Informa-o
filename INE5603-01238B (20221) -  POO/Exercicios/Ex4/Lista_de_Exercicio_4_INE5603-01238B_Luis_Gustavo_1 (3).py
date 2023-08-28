"""
EX 1
print("Digite seu sexo")
sexo = str(input("M se for masculino e F para feminino: ")).upper()

while sexo != "M" and sexo != "F":
    print("Valor incorreto")
    sexo = input("Tente novamente: ")
if sexo == "M":
    print("Você selecionou masculino")
elif sexo == "F":
    print("Você selecionou feminino")
"""
"""
EX 2
from random import randrange
num = randrange(11)
tent = 1
numEscolhido = int(input("Escolha um número de 0 a 10: "))
while num != numEscolhido:
    numEscolhido = int(input("ERROU!!! Tente novamente: "))
    tent += 1
print(f"ACERTOU!!!\n Em apenas {tent} tentativas.")
"""
"""
EX 3
desconto = 0
p = 0
salario = float(input("Digite o salário: "))
r = str(input("Deseja descontar do salário? "))
while r == "Sim":
    if salario * 0.11 > 320:
        desconto = 320
        p = 32000/salario
        print(f"{p}% de desconto.")
    else:
        desconto = salario * 0.11
    salario = salario - desconto
    r = input("Deseja continuar descontando? ")
desconto += desconto    
print("O desconto é:",desconto)
"""
"""
EX 4
n = int(input("Digite um número inteiro entre 1 e 10000: "))
for i in range (1,10000):
    if i % n==2:
        print(i)
"""
"""
EX FIBONACCI
num1 = 0
num2 = 1
cont = 0
n = int(input("Escolha a quantidade de números da sequencia de Fibonacci "))
while n > cont:
    if cont % 2 == 0:
        print(num1)
        num1 = num2 + num1
    else:
        print(num2)
        num2 = num2 + num1
    cont += 1
"""
"""
EX 5
t = 1
n = int(input("Digite um número e veja sua tabuada "))
while t < 11:
    m = n * t
    print(n,"x",t,"=",m)
    t += 1
"""
"""
EX 6
e = ''
x = int(input("Digite um número "))

for i in range(1,x+1):
    e += str(i) + " "
print(e)
"""
"""
n, a, g, d = 0, 0, 0, 0
print(" 1. Alcool \n 2. Gasolina \n 3. Diesel \n 4. Finalizar pedido")
while (n != 4):
    n = int(input("Selecione o que deseja: "))
    if n == 1:
        a += 1
    elif n == 2:
        g += 1
    elif n == 3:
        d += 1
print("MUITO OBRIGADO\nAlcool: {}\nGasolina: {}\nDiesel: {}".format(a, g, d))
"""
"""
EX 7
num1 = 0
num2 = 0
e = ' '
soma = 0
while num1 <= 0 or num2 <= 0:
    num1 = int(input("Selecione um número: "))
    num2 = int(input("Selecione outro número: "))
    print("Tente números maiores que 0")
if num1 > num2:
    for i in range(num2, num1 + 1):
        e += str(i) + " "
        soma += i
    print(e, 'Soma = ',soma)
elif num2 > num1:
    for i in range(num1, num2 + 1):
        e += str(i) + " "
        soma += i
    print(e, 'Soma = ',soma)
"""
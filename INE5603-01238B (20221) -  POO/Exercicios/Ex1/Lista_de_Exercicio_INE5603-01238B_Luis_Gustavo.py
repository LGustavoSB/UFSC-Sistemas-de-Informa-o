"""
Exercício 1

a = int(input("escolha um número"))
b = int(input("escolha outro número"))
soma = a + b
print("SOMA =", soma)
"""
"""
Exercicio 2 

a = int(input("escolha um número"))
b = int(input("escolha outro número"))
prod = a * b
print("PROD =", prod)
"""
"""
Exercicio 3 

a = float(input("escolha um número"))
b = float(input("escolha outro número"))
A = a * 3.5
B = b * 7.5
media = (A + B)/11
print("MEDIA = {:.5f}".format(media))
"""
"""
Exercicio 4

a = float(input("escolha um número"))
b = float(input("escolha outro número"))
c = float(input("escolha outro número"))
A = a * 2
B = b * 3
C = c * 5
media = (A + B + C)/10
print("MEDIA =", media)
"""
"""
Exercicio 5

a = int(input("escolha um número"))
b = int(input("escolha outro número"))
c = int(input("escolha mais um número"))
d = int(input("escolha outro número"))
diferenca = (a * b) - (c * d)
print('DIFERENCA =', diferenca)
"""
"""
Exercicio 6

employeeNum = int(input("Qual a numeração do empregado?"))
hours = int(input("Trabalha quantas horas por mês?"))
money = float(input("Quanto ganha por hora?"))
salary = hours * money
print('NUMBER =', employeeNum)
print('SALARY = U$', salary)
"""
"""
Exercicio 7

N = int(input("Pressão desejada"))
M = int(input("Pressão lida pela bomba"))
diferenca = N - M
print(diferenca)
"""
"""
Exercicio 8

t = int(input("Quantas pessoas acessaram o terceiro link?"))
p = t * 4
print(p)
"""
"""
Exercicio 9

a = float(input("Qual o valor de A?"))
b = float(input("Qual o valor de B?"))
c = float(input("Qual o valor de C?"))
tri = (a * c)/2
cir = 3.14159 * c ** 2
tra = ((a + b) * c) / 2
qua = b ** 2
ret = a * b
print("TRIANGULO: {:.3f}".format(tri))
print("CIRCULO: {:.3f}".format(cir))
print("TRAPEZIO: {:.3f}".format(tra))
print("QUADRADO: {:.3f}".format(qua))
print("RETANGULO: {:.3f}".format(ret))
"""
"""
Exercicio 10

age = int(input("Digite sua idade em dias"))
y = age // 365
m = (age % 365) // 30
d = age % 365 % 30
print(y, "ano(s)")
print(m, "mes(es)")
print(d, "dia(s)")
"""
"""
Exercicio 11

import math
x1 = float(input("Valor de x1 "))
y1 = float(input("Valor de y1 "))
x2 = float(input("Valor de x2 "))
y2 = float(input("Valor de y2 "))
d = (x2 - x1) ** 2 + (y2 - y1) ** 2
print ("{:.4f}".format(math.sqrt(d)))
"""
"""
Exercicio 12

N = int(input("Tempo em segundos "))
h = N // 3600
m = (N % 3600) // 60
s = N % 3600 % 60
print(h,":",m,":",s)
"""
"""
Exercicio 13

t = int(input("Quantas horas a viagem durou? "))
v = int(input("Qual a velocidade média? "))
d = v * t
l  = d/12
print("{:.3f}".format(l))
"""
"""
Exercicio 14

x = int(input("Quantos quilometros feitos? "))
y = float(input("Quantos litros gastos? "))
z = x / y
print("O consumo médio é de {:.3f}".format(z),"km/l")
"""
"""
Exercicio 15

n = input("Nome do empregado ")
s = float(input("Salário "))
pV = float(input("Produtos vendidos "))
b = float(pV * (0.15))
total = s + b
print("TOTAL = R$ {:.2f}".format(total))
"""
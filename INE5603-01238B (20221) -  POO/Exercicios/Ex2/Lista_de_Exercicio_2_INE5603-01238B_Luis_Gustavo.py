"""
Exercicio 1

s = float(input("Salário "))
if 0.00 <= s <= 2000.00:
    print("ISENTO")
elif 2000 < s <= 3000.00:
    s1f = (s - 2000) * 0.08
    print("R$ {:.2f}".format(s1f))
elif 3000 < s <= 4500.00:
    s2 = (s - 3000) * 0.18
    s2f = s2 + 80
    print("R$ {:.2f}".format(s2f))
elif s > 4500.00:
    s3 = (s - 4500) * 0.28
    s3f = s3 + 270 + 80
    print("R$ {:.2f}".format(s3f))
"""
"""
Exercicio 2

ddd = input("DDD ")
if (ddd == "61"):
    print("Brasilia")
elif ddd == "71":
    print("Salvador")
elif ddd == "11":
    print("Sao Paulo")
elif ddd == "21":
    print("Rio de Janeiro")
elif ddd == "32":
    print("Juiz de Fora")
elif ddd == "19":
    print("Campinas")
elif ddd == "27":
    print("Vitoria")
elif ddd == "31":
    print("Belo Horizonte")
else:
    print("DDD não cadastrado")
"""
"""
Exercicio 3

n = int(input("Digite o número do mês "))
if n == 1:
    print("January")
elif n == 2:
    print("February")
elif n == 3:
    print("March")
elif n == 4:
    print("April")
elif n == 5:
    print("May")
elif n == 6:
    print("June")
elif n == 7:
    print("July")
elif n == 8:
    print("August")
elif n == 9:
    print("September")
elif n == 10:
    print("October")
elif n == 11:
    print("November")
elif n == 12:
    print("December")
else:
    print("Não é um mês")
"""
'''
Exercicio 4

a = float(input("Valor de A "))
b = float(input("Valor de B "))
c = float(input("Valor de C "))
d = (b**2)-(4*a*c)
if(d < 0 or a == 0):
    print("Impossivel calcular")
else:
    d= d ** 0.5
    r1 = (-b + d) / (2 * a)
    r2 = (-b - d) / (2 * a)
    print(f'r1 = {r1:0.5f}\nr2 = {r2:0.5f}')
'''
'''
Exercicio 5

a,b,c = input("Qual a pontuação de A, B e C? ").split()
if a > b > c or c > b > a:
    print(f"O vice-campeão foi B com {b} pontos")
elif b > a > c or c > a > b:
    print(f"O vice-campeão foi A com {a} pontos")
elif a > c > b or b > c > a:
    print(f"O vice-campeão foi C com {c} pontos")
'''
"""
Exercicio 6

cv, ce, cs, fv, fe , fs = map(int, input().split())
tc = (cv*3) + ce
tf = (fv*3) + fe

if tc > tf:
    print('C')
elif tc < tf:
    print('F')
elif tc == tf and fs == cs:
    print('=')
elif tc == tf and fs > cs:
    print('F')
elif tc == tf and fs < cs:
    print('C')
"""
"""
Exercicio 9

i = int(input())
f = int(input())
if(i < f):
    t = f - i
else:
    t = f + 24 - i
print(f"O JOGO DUROU {t} HORA(S)")
"""
'''
Exercicio 10

iH = int(input())
iM = int(input())
fH = int(input())
fM = int(input())
tH = fH - iH
if(tH < 0):
    tH = 24 + (fH - iH)
tM = fM - iM
if(tM < 0):
     tM = 60 + (fM - iM)
     tH = tH - 1
if (iH == fH and iM == fM):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print(f"O JOGO DUROU {tH} HORA(S) E {tM} MINUTO(S)")
'''
"""
Ex 7, 8, 11, 12, 13 não feitos.
"""

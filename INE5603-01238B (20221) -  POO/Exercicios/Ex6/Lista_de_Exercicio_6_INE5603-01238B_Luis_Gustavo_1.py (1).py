"""
EX 1
def aumento(salario):
    if salario <= 400:
        percent = "15%"
        reajuste = salario * 0.15
    elif salario <= 800:
        percent = "12%"
        reajuste = salario * 0.12
    elif salario <= 1200:
        percent = "10%"
        reajuste = salario * 0.10
    elif salario <= 2000:
        percent = "7%"
        reajuste = salario * 0.07
    elif salario > 2000:
        percent = "4%"
        reajuste = salario * 0.04
    novo_salario = salario + reajuste
    print(f"Novo Salário: {novo_salario}\nAumento no Salário: {reajuste}\nPercentual Aplicado: {percent}")
aumento(float(input("Qual seu salário? ")))
"""
"""
EX 2
def mudar_horas(hora_saida, tempo, fuso):
    hora_chegada = (hora_saida + tempo) + fuso
    if hora_chegada >= 24:
        hora_chegada -= 24
    if hora_chegada < 0:
        hora_chegada += 24
    print(f"O horário do local atual é {hora_chegada}hr.")
mudar_horas(int(input("Qual a hora da saída? ")),int(input("Quanto dura o voo? ")),int(input("Qual o fuso horario do local? ")))
"""
"""
EX 3
def total_soma(num_x, num_z):
    cont = 1
    soma = num_x
    while num_z <= num_x:
        print("OOOPS, Z deve ser maior que X")
        num_z = int(input("Digite outro número: "))
    while soma <= num_z:
        num_x += 1
        cont += 1
        soma += num_x
    print(cont)
total_soma(int(input("Digite um número para X: ")), int(input("Digite outro número, agora para Z: ")))
"""
"""
EX 4
def coord(ponto_x, ponto_y):
    if ponto_x > 0 and ponto_y > 0:
        print("Primeiro")
    elif ponto_x < 0 and ponto_y > 0:
        print("Segundo")
    elif ponto_x < 0 and ponto_y < 0:
        print("Terceiro")
    elif ponto_x > 0 and ponto_y < 0:
        print("Quarto")
    elif ponto_x == 0 and ponto_y == 0:
        print("O ponto está na origem")
    elif ponto_x == 0:
        print("O ponto está no eixo das abscissas")
    else:
        print("O ponto está no eixo das ordenadas")
coord(int(input("Qual o valor do ponto x? ")), int(input("E do ponto y? ")))
"""
"""
EX 5
def capacidade_carga(num_andares, max_carga):
    cont = 0
    total_pessoas = 0
    for i in range(num_andares):
        entrada = int(input("Quantos entraram? "))
        total_pessoas += entrada
        saida = int(input("Quantos saíram? "))
        total_pessoas -= entrada
        if total_pessoas > max_carga:
            cont += 1
    if cont > 0:
        print("A carga máxima foi ultrapassada")
    else:
        print("A carga máxima foi respeitada")
capacidade_carga(int(input("Em quantos andares o elevador parou? ")),int(input("Qual a capacidade máxima de carga do elevador? ")))
"""
"""
EX 6
def teste_porta(a,b,c,h,l):
    if h < l:
        x = h
        h = l
        l = x
    if h >= a and (l >= b or l >= c) or h >= b and (l >= a or l >= c) or h >= c and (l >= a or l >= b):
        resp = "Parabens pela aquisiçao!"
    else:
        resp = "Ops, o colchao nao passa pela porta, procure outro!"
    return resp
resp_final = teste_porta(int(input("Espessura do colchão? ")),int(input("Largura do colchão? ")),int(input("Altura do colchão? ")),int(input("Altura da porta? ")),int(input("Largura da porta? ")))
print(resp_final)
"""
"""
EX 7
def melhor_aluno():
    notaMaior = 0
    alunoMaior = 0
    for i in range (1,6):
        nota = float(input(f"Digite a nota do aluno {i}: "))
        if nota > notaMaior:
            notaMaior = nota
            alunoMaior = i
        if notaMaior >= 5.75:
            cond = "Aprovado"
        elif notaMaior < 5.75 and notaMaior >= 2.75:
            cond = "Em REC"
        elif notaMaior < 2.75:
            cond = "Reprovado"
    print(f"O aluno {alunoMaior} obteve a melhor pontuação, estando {cond} neste semestre")
    return notaMaior
melhorAluno = melhor_aluno()
print("com nota: ", melhorAluno)
"""
"""
EX 8
def teste_numero():
    par, impar = 0, 0
    for i in range(10):
        num = int(input("Digite um numero: "))
        if num % 2 == 0:
            print("O número digitado é PAR")
            par += 1
        elif num % 2 != 0:
            print("O número digitado é IMPAR")
            impar += 1
        total_num = f"Dos 10 números escolhidos, {par} eram PAR e {impar} eram IMPAR"
    return total_num
print("Escolha 10 numeros")
result_final = teste_numero()
print(result_final)
"""
"""
EX 9
def teste_numero(num1, num2):
    div, primos = 0, 0
    for i in range (num1, num2+1):
        div = 0
        for x in range (1, i+1):
            if (i % x) == 0:
                div = div + 1        
        if (div == 2):
            primos += 1
    return primos 
primos_final =teste_numero(int(input("Digite um número: ")),int(input("Digite outro número, maior que o primeiro: ")))
print(f"Entre esses dois números há {primos_final} número primos")
"""
"""
EX 10
def media_idades():
    soma, cont = 0, 0
    print("Para parar, digite um número negativo!")
    while True:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            break
        soma += idade
        cont += 1
    media = soma / cont
    return media
media_final = media_idades()
print(media_final)
"""
"""
EX 11
def num_positivos():
    soma, cont = 0, 0
    for i in range(6):
        num = float(input("Digite um número"))
        if num > 0:
            soma += num
            cont += 1
    media = soma / cont
    result = f"{cont} valores positivos\n{media}"
    return result
result_final = num_positivos()
print(result_final)
"""
"""
EX 12
def contador(inicio, fim, passo):
    if inicio > fim:
        passo = -passo
    for i in range (inicio, fim+1, passo):
        print(i)
contador(int(input("Digite o numero de inicio: ")),int(input("Digite o numero final: ")),int(input("Digite o passo da contagem: ")))
"""
"""
EX 13
def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f"O terreno terá área total de {area_terreno}m²")
print("Calcule a area do terreno retangular")
area(int(input("Qual a largura do terreno? ")),int(input("E o comprimento? ")))
"""
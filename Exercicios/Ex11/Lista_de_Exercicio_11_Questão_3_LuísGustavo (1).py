numEntrevistados = int(input("Quantas pessoas foram entrevistadas?"))
while not(4 < numEntrevistados < 233000):
    print("NUMERO INVALIDO! Deve existir um minimo de 4 e um maximo de 233000 entrevistados")
    numEntrevistados = int(input("Quantas pessoas foram entrevistadas?"))

respLista = list(input("Digite 0 se estiver ok e 1 se não estiver\nFaça no formato [n n n n n...]: ").split(" "))
while len(respLista) != numEntrevistados:
    respLista = list(input("Quantidade de entrevistados diferente da quantidade de respostas, digite novamente: ").split(" "))
qtd0 = respLista.count("0")
qtd1 = respLista.count("1")

if qtd0 > qtd1:
    print("Y")
elif qtd1 >= qtd0:
    print("N")
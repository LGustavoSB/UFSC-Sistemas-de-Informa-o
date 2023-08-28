def verifica_num():
    


while True:
    matriz = []
    nova_matriz = []
    num_colunas, num_linhas = [int(x) for x in input("Tamanho da Matriz, Digite no formato:\nNumero de colunas x Numero de linhas: ").split(' x ')]
    if num_linhas == 0 or num_colunas == 0:
        break
    
    print('Digite [1] se houver mina ou [0] se não houver\n')

    for linha in range(num_linhas):
        lista_linha = []
        for coluna in range(num_colunas):
            num = verifica_num(int(input(f'[{linha},{coluna}]: ')))
            lista_linha.append(num)
        matriz.append(lista_linha)

    print('Campo Minado Original')
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            print(f'[ {matriz[linha][coluna]} ]', end=' ')
        print()
        
    print('-='*3*num_colunas)

    for linha in range(num_linhas):
        lista_linha = []
        for coluna in range(num_colunas):
            if matriz[linha][coluna] == 1:
                lista_linha.append(9)
            else:
                num_minas = 0
                if linha == 0 and coluna == 0:
                        if matriz[linha+1][coluna] == 1:
                            num_minas += 1
                        if matriz[linha][coluna+1] == 1:
                            num_minas += 1
                elif linha == 0:
                    if coluna == num_colunas-1:
                        if matriz[linha+1][coluna] == 1:
                            num_minas += 1
                        if matriz[linha][coluna-1] == 1:
                            num_minas += 1
                    elif coluna != 0:
                        if matriz[linha+1][coluna] == 1:
                            num_minas += 1
                        if matriz[linha][coluna-1] == 1:
                            num_minas += 1
                        if num_colunas > 2:
                            if matriz[linha][coluna+1] == 1:
                                num_minas += 1
                elif coluna == 0:
                    if linha == num_linhas-1:
                        if matriz[linha][coluna+1] == 1:
                            num_minas += 1
                        if matriz[linha-1][coluna] == 1:
                            num_minas += 1
                    elif linha != 0:
                        if matriz[linha-1][coluna] == 1:
                            num_minas += 1
                        if matriz[linha][coluna+1] == 1:
                            num_minas += 1
                        if num_linhas > 2:
                            if matriz[linha+1][coluna] == 1:
                                num_minas += 1
                elif linha == num_linhas-1:
                    if coluna == num_colunas-1:
                        if matriz[linha][coluna-1] == 1:
                            num_minas += 1
                        if matriz[linha-1][coluna] == 1:
                            num_minas += 1
                    elif coluna != 0:
                        if matriz[linha-1][coluna] == 1:
                            num_minas += 1
                        if matriz[linha][coluna-1] == 1:
                            num_minas += 1
                        if matriz[linha][coluna+1] == 1:
                            num_minas += 1 
                elif coluna == num_colunas-1:
                    if matriz[linha][coluna-1] == 1:
                        num_minas += 1
                    if matriz[linha-1][coluna] == 1:
                        num_minas += 1
                    if matriz[linha+1][coluna] == 1:
                        num_minas += 1
                else:
                    if matriz[linha+1][coluna]:
                        num_minas += 1
                    if matriz[linha-1][coluna]:
                        num_minas += 1
                    if matriz[linha][coluna+1]:
                        num_minas += 1
                    if matriz[linha][coluna-1]:
                        num_minas += 1
                    
                lista_linha.append(num_minas)
                      
        nova_matriz.append(lista_linha)
        
    for linha in range(num_linhas):
        for coluna in range(num_colunas):
            print(f'[ {nova_matriz[linha][coluna]} ]', end=' ')
        print()

print('fim de execução')
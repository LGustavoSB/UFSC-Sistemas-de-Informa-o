'''Crie um programa de cadastro de pessoas  (cadastrar utilizando a estrutura de dicionário)
Neste cadastro as seguintes informações devem ser inseridas:
-  nome, ano de nascimento e carteira de trabalho (o programa irá ler do teclado o ano de nascimento, mas deve armazenar no dicionário a idade do funcionário).
Se o número da carteira de trabalho for diferente de zero, o dicionário deverá armazenar também as seguintes informações:
- o ano de contratação, o salário e a idade em que a pessoa irá se aposentar (para o cálculo da estimativa da idade da aposentadoria considere 35 anos de contribuição).
Imprimir os dados do dicionário recém gerado.
Sugestão de implementação, utilizar um menu com as seguintes opções;
1)Cadastrar usuário
2)Imprimir dados (pesquisar pelo nome)
3)Imprimir dados (todos os usuários)
4)Encerrar o programa
'''
def opcao_1():
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = 2022 - int(input('Ano de Nascimento: '))
    pessoa['ctps'] = input('Ctps: ')
    if pessoa['ctps'] == '0':
        ctps = False
    else:
        ctps = True
        pessoa['anoDeContratação'] = int(input('Ano de Contratação: '))
        pessoa['salario'] = int(input('Salario: '))
        pessoa['idadeAposentadoria'] = (pessoa['idade'] + pessoa['anoDeContratação'] + 35) - 2022
    
    cadastros.append(pessoa.copy())
    print()


def opcao_2():
    nome = input('Qual o nome? ')    
    cadastrado = cadastros.get('nome', 'Nome não cadastrado')   


def opcao_3():
    for p in cadastros:
        print('-='*35)
        for k,v in p.items():
            print(f'{k}: {v}')
    

pessoa = dict()
cadastros = list()  
while True:
    escolha = input('Qual ação você deseja tomar?' +
                    '\n1)Cadastrar usuário' +
                    '\n2)Imprimir dados (pesquisar pelo nome)' +
                    '\n3)Imprimir dados (todos os usuários)' +
                    '\n4)Encerrar o programa 1\n')
    if escolha == '1':
        opcao_1()
    elif escolha == '2':
        opcao_2()
    elif escolha == '3':
        opcao_3()
    elif escolha == '4':
        break

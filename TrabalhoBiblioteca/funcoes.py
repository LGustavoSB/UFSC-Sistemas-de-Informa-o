from classes import *
from datetime import datetime


def login():
  while True:
    username = input('Usuario: ')
    for funcionario in lista_funcionarios:
      valido = True
      if username == funcionario.get_id():
        senha = input('Senha: ')
        if senha == funcionario.get_senha():
          print(f'\nBem vindo, {funcionario.get_nome()}!\n')
          return funcionario.get_nome()
        else:
          valido == False

def logout(func_log):
  print(f'\nAté a proxima, {func_log}')
  while True:
    resp = input('\nDeseja fechar o programa? [S/N]: ')
    if resp not in 'sSnN' or resp == '':
      print('\nOpção Inválida. Tente Novamente\n')
      continue
    else:
      break
  return resp


#---------------------------------------------------------------------------------------------
#------FUNÇOES CLIENTES-----------------------------------------------------------------------
#FUNÇAO PARA CADASTRAR NOVOS CLIENTES
def cadastrar_cliente(c_c):
    c_c += 1
    print('\n------ CADASTRAR CLIENTE ------\n')
    while True:
        nome_cliente = input('Nome: ')
        if nome_cliente in '':
            print('Digite algo')
            continue
        break
    while True:
        cargo_cliente = input('Cargo na Instituição [aluno/professor]: ')
        if cargo_cliente.lower() not in 'alunoprofessor' or cargo_cliente in '':
            print('Cargo inválido')
            continue
        break
          
    cliente = Cliente(nome_cliente,('00'+str(c_c)),cargo_cliente.capitalize())
    lista_clientes.append(cliente)
    print('\n------ CADASTRO REALIZADO ------\n')
#---------------------------------------------------------------------------------------------
#FUNÇAO PARA MOSTRAR LISTA DE CLIENTES
def mostrar_lista_clientes():
  print('\n------ CLIENTES ------\n')
  for cliente in lista_clientes:
    print(cliente.get_dados())
#---------------------------------------------------------------------------------------------
#FUNÇAO PARA EXCLUIR CLIENTE DA LISTA DE CLIENTES
def excluir_cliente():
  print('\n------ DELETAR CLIENTE ------\n')
  id_cliente_excluido = input('Qual o ID do cliente que será excluido? ')
  for i, o in enumerate(lista_clientes):
    if id_cliente_excluido == o.get_id():
      del lista_clientes[i]
      break
  print(f'CONTA DO CLIENTE {o.get_nome()} DELETADA!')
#---------------------------------------------------------------------------------------------

#------FUNÇOES LIVRO--------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
#FUNÇAO PARA ADICIONAR LIVRO NA BIBLITOECA
def cadastrar_livro(c_l):
  c_l += 1
  print('\n------ CADASTRAR LIVRO ------\n')
  while True:
    titulo = input('Titulo: ')
    if titulo in '':
      print('Digite algo')
      continue
    break
  while True:
    autor = input('Autor: ')
    if autor in '':
      print('Digite algo')
      continue
    break
  while True:
    try:
      data_publicacao = input('Data de Publicação [dd/mm/aaaa]: ')
      data = datetime.strptime(data_publicacao, '%d/%m/%Y')
      break
    except ValueError:
      print('\nFORMATO DE DATA INVALIDO\n')
  livro = Livro(titulo,autor,'00'+str(c_l),data_publicacao)
  lista_livros.append(livro)
  print('\n------ CADASTRO REALIZADO ------\n')
#---------------------------------------------------------------------------------------------
#FUNÇAO PARA VER LISTA DE LIVROS DA BIBLITOECA
def mostrar_lista_livros():
  print('\n------ LIVROS ------\n')
  for livro in lista_livros:
    print(livro.get_infos())  
#---------------------------------------------------------------------------------------------
#FUNÇAO PARA EXCLUIR LIVRO DA BIBLITOECA
def excluir_livro():
  print('\n------ DELETAR LIVRO ------\n')
  id_livro_excluido = input('Qual o ID do livro que será excluido? ')
  for num, livro in enumerate(lista_livros):
    if id_livro_excluido == livro.get_id():
      del lista_livros[num]
      break
  print(f'\nLIVRO {livro.get_titulo()} DELETADO!\n')
#---------------------------------------------------------------------------------------------
#------FUNÇOES FUNCIONARIOS-----------------------------------------------------------------------
#FUNÇAO PARA CADASTRAR NOVOS FUNCIONARIOS
def cadastrar_funcionario():
    print('\n------ CADASTRAR FUNCIONARIO ------\n')
    while True:
        nome_funcionario = input('Nome: ')
        if nome_funcionario in '':
            print('Digite o nome')
            continue
        break
    while True:
        username_funcionario = input('Nome de usuario: ')
        if username_funcionario in '':
            print('Digite o nome de usuario')
            continue
        break
    while True:
        senha_funcionario = input('Senha: ')
        if senha_funcionario in '':
            print('Digite a senha')
            continue
        break
    funcionario = Funcionario(nome_funcionario, username_funcionario, senha_funcionario)          
    lista_funcionarios.append(funcionario)
    print('\n------ CADASTRO REALIZADO ------\n')
#---------------------------------------------------------------------------------------------
#FUNÇAO PARA MOSTRAR LISTA DE CLIENTES
def mostrar_lista_funcionarios():
  print('\n------ FUNCIONARIOS ------\n')
  for funcionario in lista_funcionarios:
    print(funcionario.get_dados())
#---------------------------------------------------------------------------------------------
def alterar_senha_funcionario():
  print('\n------ MUDAR SENHA ------\n') 
  while True:
    id_funcionario = input('Id do funcionario terá a senha mudada: ')
    for num,func in enumerate(lista_funcionarios):
      verifica = True
      if id_funcionario == func.get_id():
        lista_funcionarios[num].set_senha(input('Nova senha: '))
        break
      else:
        verifica = False
    if verifica == False:
      print('FUNCIONARIO NAO ENCONTRADO')
      continue
    else:
      break
  print('\n------ SENHA ATUALIZADA ------\n')
#FUNÇAO PARA EXCLUIR FUNCIONARIO DA LISTA DE FUNCIONARIOS
def excluir_funcionario():
  print('\n------ DELETAR FUNCIONARIO ------\n')
  while True:
    id_funcionario_excluido = input('Qual o Username do funcionário que será excluido? ')
    for num, user in enumerate(lista_funcionarios):
      verifica = True
      if id_funcionario_excluido == user.get_id():
        del lista_funcionarios[num]
        break
      else:
        verifica = False
    if verifica == False:
      print('USERNAME NAO ENCONTRADO')
      continue
    else:
      break
  print(f'CONTA DO FUNCIONARIO {user.get_nome()} DELETADA!')
#---------------------------------------------------------------------------------------------
#----FUNÇOES EMPRESTIMOS----------------------------------------------------------------------
#FUNÇAO PARA EMPRESTAR LIVROS
def realizar_emprestimo():
  print('\n------ EMPRESTIMO ------\n')
  while True:
    cliente_emprestimo = input('\nID do Cliente: ')
    for cliente in lista_clientes:
        valido = True
        if cliente_emprestimo == cliente.get_id():
            nome_aluguel = cliente.get_nome()
            break
        else:
            valido = False
    if valido == False:
        print('\nCLIENTE:ID INVALIDO\n')
        continue
    break
  while True:
    livro_emprestado = input('ID do Livro: ')
    for livro in lista_livros:
      if livro_emprestado == livro.get_id():
        if livro.get_status() == 'Indisponivel':
          valido = False
          break
        resp = (f'\nO livro {livro.get_titulo()} foi emprestado para {nome_aluguel}\n')
        valido = True
        livro.set_status('Indisponivel')
      else:
        valido == False
    if valido == False:
      print('\nLIVRO NAO ENCONTRADO OU INDISPONIVEL\n')
    else: 
      print(resp)
      break
  data_emprestimo = datetime.now()
  dados_emprestimo = {'livro':livro_emprestado,'nome':nome_aluguel, 'data':data_emprestimo.strftime('%d/%m/%Y')}
  lista_livros_alugados.append(dados_emprestimo)
#---------------------------------------------------------------------------------------------
#FUNÇAO PARA VER LISTA DE LIVROS EMPRESTADOS
def mostar_lista_emprestimos():
  print('\n------ LIVROS ALUGADOS ------\n')
  for livro in lista_livros_alugados:
    for v in livro.values():
      print(v, end=' | ')
    print()
#---------------------------------------------------------------------------------------------
#FUNÇAO PARA CALCULAR ATRASO EM DEVOLUÇÃO-----------------------------------------------------
def calcular_atraso():
  for livro in lista_livros_alugados:
    atraso = (datetime.today() - datetime.strptime(livro['data'], '%d/%m/%Y')).days
    if atraso >= 7:
      multa = atraso*taxa_diaria
      situacao = str('Id Livro:{}  | Situação: ATRASADO | {} Dias | Multa: R${}').format(livro['livro'],(atraso-7),multa)
      atrasos.append(situacao)
#---------------------------------------------------------------------------------------------
#FUNÇAO PARA VER LISTA DE DEVOLUÇOES ATRASADAS------------------------------------------------
def mostrar_relatorio_atrasados():
  calcular_atraso()
  print('\n------ DEVOLUÇÕES ATRASADAS ------\n')
  if len(atrasos) == 0:
    print('NENHUMA DEVOLUÇÃO ATRASADA')
  else:
    for devolucao_atrasada in atrasos:
      print(devolucao_atrasada)
#---------------------------------------------------------------------------------------------
#FUNÇAO PARA DAR BAIXA EM DEVOLUÇÃO
def receber_devolucao():
  print('\n------DEVOLUÇÃO------')
  while True:
    id_livro_devolvido = input('Qual o ID do livro que está sendo devolvido? ')
    for num, livro in enumerate(lista_livros_alugados):
      valida = True
      if id_livro_devolvido == livro['livro']:
        del lista_livros_alugados[num]
        for livr in lista_livros: 
          if livr.get_id() == id_livro_devolvido:
            livr.set_status('Disponivel')
        break
      else:
        valida = False
    if valida == False:
      print('EMPRESTIMO NAO ENCONTRADO')
      continue
    break
  print('\nLIVRO DE {} DEVOLVIDO!\n'.format((livro['nome'])))
  atraso = (datetime.today() - datetime.strptime(livro['data'], '%d/%m/%Y')).days
  if atraso >= 7:
    multa = atraso*taxa_diaria
    print(f'ATRASO DE {atraso-7} DIAS\nVALOR DA MULTA: R${multa:.2f}')
  else:
    print('DEVOLUÇÃO SEM ATRASO')

#---------------------------------------------------------------------------------------------
#------DADOS BASE-----------------------------------------------------------------------------
def dados_base():
  livro001 = Livro('As Cronicas de Narnia - Volume Único','C.S. Lewis','001','01/01/2019')
  livro002 = Livro('Principia Mathematica - Volume 1','A.N.Whithehead & B. Russel','002','21/02/2009')
  livro003 = Livro('O Pequeno Principe','Antoine de Saint-Exupéry','003','01/02/2015')
  livro004 = Livro('Pense em Python: Pense Como um Cientista da Computação','Allen. B. Downey','004','07/06/2016')
  lista_livros.append(livro001)
  lista_livros.append(livro002)
  lista_livros.append(livro003)
  lista_livros.append(livro004)
  cliente1 = Cliente('Arthur','001','Professor')
  cliente2 = Cliente('Luis','002','Aluno')
  cliente3 = Cliente('Carlos Alberto','003','Aluno')
  lista_clientes.append(cliente1)
  lista_clientes.append(cliente2)
  lista_clientes.append(cliente3)
  funcionario1 = Funcionario('José Paulo','jose','270503')
  funcionario2 = Funcionario('Ana Maria','ana1234','ana1234')
  admin = Funcionario('Administrador','adm123','senha')
  lista_funcionarios.append(admin)
  lista_funcionarios.append(funcionario1)
  lista_funcionarios.append(funcionario2)
  while True:
    cliente_emprestimo = '001'
    for cliente in lista_clientes:
      if cliente_emprestimo == cliente.get_id(): 
        break
    livro_emprestado = '002'
    for livro in lista_livros: 
      if livro_emprestado == livro.get_id(): 
        livro.set_status('Indisponivel')
        break
    data_emprestimo = datetime(2022,12,2)
    dados_emprestimo = {'livro':livro.get_id(),'nome':cliente.get_nome(), 'data':data_emprestimo.strftime('%d/%m/%Y')}
    lista_livros_alugados.append(dados_emprestimo) 
    break

taxa_diaria = float(1)
codigo_cliente = 3
codigo_livro = 4
lista_clientes = []
lista_livros = []
lista_funcionarios = []
lista_livros_alugados = []
atrasos = []
dados_base()
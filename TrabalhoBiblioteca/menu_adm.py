from funcoes import * 
from classes import *


def menu_admin(func_log):
  while True:
    print('''------ BIBLIOTECA ------\n
    \r[1] Controle de Clientes
    \r[2] Controle de Livros
    \r[3] Controle de Emprestimos
    \r[4] Controle de Funcionarios
    \r[0] Sair
      ''')
    opc = input('Escolha uma opção: ')
    print()
    if opc == '1':
      opc = opc_controle_cliente()
      if opc == '0':
        continue
    elif opc == '2':
      opc = opc_controle_livro()
      if opc == '0':
        continue
    elif opc == '3':
      opc = opc_controle_emprestimos()
      if opc == '0':
        continue 
    elif opc == '4':
      opc = opc_controle_funcionarios()
      if opc == '0':
        continue
    elif opc == '0':
        resp = logout(func_log)
        break
    else: 
      print('OPÇÃO INVALIDA')
    input()
  return resp


def opc_controle_cliente():
    while True:
        print('''\n------ CONTROLE CLIENTES -------\n
      \r[1] Cadastrar Cliente
      \r[2] Lista de Clientes
      \r[3] Excluir Cliente
      \r[0] Voltar
      ''')
        opc = input(': ')
        if opc == '1':
          cadastrar_cliente(codigo_cliente)
          break
        elif opc == '2':
          mostrar_lista_clientes()
          break
        elif opc == '3':
          excluir_cliente()
          break
        elif opc == '0':
          return '0'
        else:
          print('OPÇÃO INVALIDA')
          continue


def opc_controle_livro():
    while True:
      print('''\n------ CONTROLE LIVROS -------\n
      \r[1] Cadastrar Livro
      \r[2] Lista de Livros
      \r[3] Excluir Livro
      \r[0] Voltar
      ''')
      opc = input(': ')
      if opc == '1':
        cadastrar_livro(codigo_livro)
        break
      elif opc == '2':
        mostrar_lista_livros()
        break
      elif opc == '3':
        excluir_livro()
        break
      elif opc == '0':
        return '0'
      else:
        print('OPÇÃO INVALIDA')
        continue


def opc_controle_emprestimos():
    while True:
      print('''\n------ CONTROLE EMPRESTIMOS -------\n
      \r[1] Realizar Empréstimo
      \r[2] Lista de Empréstimos
      \r[3] Relatório de Atrasados
        \r[4] Receber Devolução 
      \r[0] Voltar
      ''')
      opc = input(': ')
      if opc == '1':
        realizar_emprestimo()
        break
      elif opc == '2':
        mostar_lista_emprestimos()
        break
      elif opc == '3':
        mostrar_relatorio_atrasados()
        break
      elif opc == '4':
        receber_devolucao()
        break
      elif opc == '0':
        return '0'
      else:
        print('OPÇÃO INVALIDA')
        continue


def opc_controle_funcionarios():
    while True:
        print('''\n------ CONTROLE FUNCIONARIOS -------\n
      \r[1] Cadastrar Funcionario
      \r[2] Lista de Funcionarios
      \r[3] Excluir Funcionario
      \r[4] Alterar Senhas
      \r[0] Voltar
      ''')
        opc = input(': ')
        if opc == '1':
          cadastrar_funcionario()
          break
        elif opc == '2':
          mostrar_lista_funcionarios()
          break
        elif opc == '3':
          excluir_funcionario()
          break
        elif opc == '4':
          alterar_senha_funcionario()
          break
        elif opc == '0':
          return '0'
        else:
          print('OPÇÃO INVALIDA')
          continue
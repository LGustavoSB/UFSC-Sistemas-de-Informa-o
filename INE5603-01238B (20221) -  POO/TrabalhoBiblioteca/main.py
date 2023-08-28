from funcoes import *
from menu_adm import *
from menu_funcionario import *
#---------------------------------------------------------------------------------------------
# INICIO DO PROGRAMA PRINCIPAL
while True:
  funcionario_logado = login()
  if funcionario_logado == 'Administrador':
    resp = menu_admin(funcionario_logado)
  else:
    resp = menu_funcionario(funcionario_logado)
  if resp in 'Ss':
    break
  else:
    continue
print('\n'*5 + 'FIM DE EXECUÇAO' + '\n'*5)
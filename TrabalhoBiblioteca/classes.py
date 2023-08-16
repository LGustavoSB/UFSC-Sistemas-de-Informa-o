
class Livro:
  def __init__(self,titulo,autor,id,data):
    self.titulo = titulo
    self.autor = autor
    self.id = id
    self.data = data
    self.status = 'Disponivel'
  def get_infos(self):
    return f'{self.id} | {self.titulo} | {self.autor} | {self.data} | {self.status}'

  def get_titulo(self):
    return self.titulo

  def get_id(self):
    return self.id

  def get_status(self):
    return self.status

  def set_status(self,new_status):
    self.status = new_status

class Pessoa:
  def __init__(self,nome,id):
    self.nome = nome
    self.id = id
  def get_nome(self):
    return self.nome
  def get_id(self):
    return self.id


class Cliente(Pessoa):
  def __init__(self,nome,id,cargo):
    super().__init__(nome,id)
    self.cargo = cargo
  def get_cargo(self):
    return self.cargo
  def get_dados(self):
    return f' {self.id} | {self.nome} | {self.cargo}'


class Funcionario(Pessoa):
  def __init__(self,nome,id,senha):
    super().__init__(nome,id)
    self.senha = senha
  def get_senha(self):
    return self.senha
  def set_senha(self,nova_senha):
    self.senha = nova_senha
  def get_dados(self):
    return ' {} | {} | {}'.format(self.nome, self.id, self.senha)
  def menu():
      menu_funcionario()


class Admin(Funcionario):
  def __init__(self,nome,id,senha):
      super().__init__(nome,id,senha)
  def menu():
      menu_admin()
    
    

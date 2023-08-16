empresa1 = list()
empresa2 = list()
    
    
    
    
while True:
    cliente = input("Qual o nome do cliente cadastrado? ")
    print("Diga em qual empresa está cadastrado: na empresa 1, na empresa 2 ou em ambas?")
    empresa = input("É cadastrado em qual das empresas? ")
    if empresa.lower() == "empresa 1":
        empresa1.append(cliente)
    elif empresa.lower() == "empresa 2":
        empresa2.append(cliente)
    elif empresa.lower() == "ambas":
        empresa1.append(cliente)
        empresa2.append(cliente)
    
    
    
    
    resp = str(input("Gostaria de cadastrar mais clientes? [S/N]: "))
    while resp.upper() != "S" and resp.upper() != "N":
        resp = input("[S/N]: ")
    if resp.upper() == "N":
        break

ep1 = set(empresa1)
ep2 = set(empresa2)
print("Numero Total de Clientes:", len(ep1.union(ep2)))
print("Todos os clientes:", ep1.union(ep2))
print("Clientes da Empresa 1", empresa1)
print("Clientes da Empresa 2",empresa2)
print("Clientes de ambas as empresas:", ep1.intersection(ep2))
print("Clientes de apenas uma das empresas:", ep1.symmetric_difference(ep2))
from super_matriz import SuperMatriz

m1 = SuperMatriz(3, 4) #instancia m1 -> matriz 3x4
m2 = SuperMatriz(5, 5) #instancia m2 -> matriz 5x5
m3 = SuperMatriz(2, 7) #instancia m3 -> matriz 2x7

m1.atribuir(2, 1, 11)
print("Valor original m1(2, 1):", m1.acessar(2, 1))
m1.atribuir(2, 1, 33)
print("Valor alterado m1(2, 1):", m1.acessar(2, 1))
print()
m2.atribuir(3, 4, 44)
print("Valor original m2(3, 4):", m2.acessar(3, 4))
m2.atribuir(3, 4, 55)
print("Valor alterado m2(3, 4):", m2.acessar(3,4))
print()
m3.atribuir(1, 5, 66)
print("Valor original m3(1, 5):", m3.acessar(1, 5))
m3.atribuir(1, 5, 77)
print("Valor alterado m3(1, 5):", m3.acessar(1, 5))

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        self.array = array_para_ordenar
        
    def ordena(self):
        for i in range(1, len(self.array)):
            i_value = self.array[i]
            x = i - 1
            while x >= 0:
                if i_value < self.array[x]:
                    self.array[x+1] = self.array[x]
                    self.array[x] = i_value
                    x = x - 1
                else:
                    break
        return self.array


    def toString(self):
        array_string = ""
        for i in range(len(self.array)):
            if i == 0:
                array_string = f"{self.array[i]}"
            else:
                array_string = array_string + f",{self.array[i]}"
        return array_string
        

def main():
    a = Ordenacao([4, 4, 1, 1, 6])
    print(a.ordena())
    print(a.toString())

main()
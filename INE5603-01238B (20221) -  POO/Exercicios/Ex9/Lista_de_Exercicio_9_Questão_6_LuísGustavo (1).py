numList = []
for i in range(10):
    num = int(input(f"Numero {i+1}: "))
    if num > 0:
        numList.append(num)
    else:
        num = 1
        numList.append(num)
    print(f"X[{i}] = {num}")
print("Lista final = {}".format(numList))
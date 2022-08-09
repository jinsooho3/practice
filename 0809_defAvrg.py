def avrgNum(argNum):
    sum = 0
    for value in range(argNum):
        num = int(input("수를 입력하세요: "))
        sum += num
    return sum / argNum

print("1")

print(avrgNum(4))

print("2")

print(avrgNum(5))
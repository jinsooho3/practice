time = 5
for value in range(time):
    for col in range(value):
        print(" ",end='')
    for col in range(time - value):
        print("*",end='')
    print()
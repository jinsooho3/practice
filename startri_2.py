line = int(input("라인 넘버 입력"))
for value in range(line):
    if value <= line //2 -1:
        for cor in range(value+1):
            print("*",end='')
    else:
        for cor in range(line - value):
            print("*",end='')
    print()
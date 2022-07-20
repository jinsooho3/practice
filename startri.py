line=int(input("라인 넘버를 입력 하세요 : "))
for value in range(line):
    if value <= (line-1)/2:     #중간값까지
        for cor_1 in range(value+1):
            print("*",end='')
    else:                       #중간값이후
        for cor_2 in range(line-value): 
            print("*",end='')
    print()

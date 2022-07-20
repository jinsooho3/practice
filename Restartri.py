num = 5
median = num // 2 + 1

for row_num in range(num):
    # *이 증가하는 반복문
    if row_num < median:
        for value in range(row_num+1):
            print("*"," ",end='')
    # *이 감소하는 반복문
    else:
        for value in range(num-row_num):
            print("*"," ",end='')
    print()
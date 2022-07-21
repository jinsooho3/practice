sum = 0
time = 5
for a in range(time):
    print(a+1,end='')
    sum += int(input("번째 값 입력 : "))

print("합계 : ", sum)
print("평균 : ",sum/time)
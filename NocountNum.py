import random
import time

alist = []
numLen = 20
for a in range(1,numLen+1):
    alist.append(a)
random.shuffle(alist)
for a in range(numLen-1):
    print(alist[a])
    time.sleep(1)
print("호출되지 않은 숫자는?")
player = int(input(""))
if player == alist[numLen-1]:
    print("정답입니다")
else:
    print("XXXXXXXXXX")
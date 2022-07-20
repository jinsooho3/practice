import random

alist=[]
for count in range(6):
     a = random.randint(1,45)
     while a in alist:
          a = random.randint(1,45)
     alist.append(a)
print(alist)
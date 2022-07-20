import random
'''
for cd in range(len(onelist)):
    chgnum=0
    for de in range(cd+1, len(onelist)):
        if onelist[cd] > onelist[de]:
            chgnum = onelist[cd]
            onelist[cd]=onelist[de]
            onelist[de]=chgnum
print(onelist)
'''
alist =[]

for a in range(10):
    alist.append(random.randint(1,30))
def mysort2 (a):
    for j in range(len(a)-1):
        for value in range(len(a) - j - 1):
            if a[value] > a[value + 1]:
                a[value] , a[value + 1] = a[value + 1], a[value]
            #print(a)
            

    print(a)
mysort2(alist)
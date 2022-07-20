#for a in range(1, 1000):
#    for b in range(1,1000):
#        for c in range(1,1000):
#            if a+b+c == 1000 and a**2 + b**2 == c**2 and a<b<c:
#                print(a,b,c)

for a in range(1, 1000):
    for b in range(1+a, 1000-a):
        c= 1000-a-b
        if a**2+b**2 == c**2:

            print(a*b*c)
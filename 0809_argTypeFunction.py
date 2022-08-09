def fox(**a):
    for k, v in a.items():
        print(k,":", v,"",end = '')
    print()

alist = [["jinsoo", "male", 80, 70],["name","male",50,90]]
for a in range(len(alist)):
    fox(name = alist[a][0], gender = alist[a][1], kor = alist[a][2], eng = alist[a][3], math = alist[a][4], )
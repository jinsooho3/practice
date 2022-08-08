def pow(a,b):
    if b == 1:
        return a
    else:
        return a*pow(a,b-1)

num1 = 3
num2 = 10
print(pow(num1, num2))
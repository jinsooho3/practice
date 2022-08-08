def factorial(a):
    if a == 1 :
        return 1
    else:
        return a * factorial(a-1)

num = int(input("팩토리얼 숫자구하기~!!"))

print(factorial(num))
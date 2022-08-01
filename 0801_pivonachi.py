def piv(n):
    if n == 1 or n == 2:
        return 1
    else:
        return piv(n-1) + piv(n-2)

num = int(input("피보나치수열 몇번째숫자? : "))
print(piv(num))
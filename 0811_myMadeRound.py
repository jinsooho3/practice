def lichou(argA):
    if argA - int(argA) < 0.5:
        return int(argA)
    else:
        return int(argA) + 1

a = 3.5
print(lichou(a))
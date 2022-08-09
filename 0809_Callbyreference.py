# 튜플은 append 자체가 안됨
def bar(a):
    a.append(4)

value = (1, 3)

bar(value)
print(value)
temp = 3

def bar():
    global temp
    print(temp)
    temp = 4
    
bar()
print(temp)
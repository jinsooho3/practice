# 특수 문자는 3개 사용 : ! . ,

myList = "!! hello world, it is awesome day."

special = 0
word = 0
totalchar = 0
for num in range(len(myList)):
    if myList[num] == ',' or myList[num] == '!' or myList[num] == '.':
        special +=1 
    elif myList[num] == ' ':
        pass
    else:
        if myList[num-1].isalpha() == False:
            word +=1
        totalchar += 1

print("특수문자 수 : ",special)
print("단어 수 : ",word)
print("특수문자 제외 글자수 : ",totalchar)
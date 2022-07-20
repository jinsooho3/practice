line = int(input("입력 문자열의 줄(line) 수를 입력하세요"))
split_value = []
just_value = []
for a in range(line):
    just_value.append(input("문자열을 입력하세요"))

searchword = input("검색할 단어를 입력하세요")
searchcount = 0
tmp = ''
searchedLine = []
wordcount = 0
for value in range(len(just_value)):
    for b in just_value[value]:
        if b != ' ':
            tmp += b
        else:
            split_value.append(tmp)
            tmp = ''
            wordcount += 1 
    split_value.append(tmp)
    tmp = ''
    wordcount += 1
    while '' in split_value:
        split_value.remove('')
        wordcount -= 1
    if searchword in split_value:
        if value not in searchedLine:
            searchedLine.append(value+1)

for a in range(len(split_value)):
    if searchword == split_value[a]:
        searchcount +=1
print(searchedLine)
print(searchcount)
print(wordcount)
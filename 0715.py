line = int(input("입력 문자열의 줄(Line) 수를 입력하세요!"))
answersplit = []

for row in range(line):
    print(row+1,end='')
    inputsen = input("문자열을 입력하세요")
    usesplit = ""
    for col in range(len(inputsen)): 
        for b in inputsen[col]:
            if b == " ":
                answersplit.append(usesplit)
                usesplit = ""
            else:
                usesplit += b
    answersplit.append(usesplit)
print(answersplit)
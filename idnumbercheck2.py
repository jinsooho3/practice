idnumber = input("주민번호 13자리를 입력해주세요")

checknum = 2
count = 0
sum = 0
while count<13:
    if idnumber[count].isdigit():
        sum += checknum * int(idnumber[count])
        checknum +=1
        if checknum >9:
            checknum = 2
    count+=1
check = (11 - (sum % 11)) % 10

if check == int(idnumber[-1]):
    print("유효한 주민번호 입니다.")
else:
    print("유효하지 않은 주민번호 입니다.")
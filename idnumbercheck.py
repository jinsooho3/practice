#주민번호 입력받기
idnumber = input("주민번호 13자리를 입력하세요 : ")   #주민번호 입력받기
checknum =2                                         #체크수
sum =0                                              #합계
for a in idnumber:                                  #입력받은 주민번호 하나하나 반복
    if a.isdigit():                                 #주민번호에서 숫자와 -를 구별
        sum += int(a)*checknum                      #숫자는 체크수와 곱해서 합계에 추가
        checknum +=1                                #체크수 증가
        if checknum >9:                             #체크수가 9를 넘으면 2로 초기화
            checknum =2

sum = sum- (checknum-1)*int(idnumber[-1])           #마지막번호를 어떻게 계산안하는거지
check = 11-(sum%11) % 10

#유효한지 아닌지 조건문
if  check == int(idnumber[-1]):
    print("유효한 주민번호 입니다")
else:
    print("유효하지 않은 주민번호 입니다")
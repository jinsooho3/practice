# 790608-2552416

# 사용자로부터 주민번호 입력
inputNum = input("번호입력")

inputNumList = []
for num in inputNum:
    #문자를 숫자로, 숫자만 리스트에 저장
    if num.isdigit():
        inputNumList.append(int(num))


#checkNum = [2,3,4,5,6,7,8,9,2,3,4,5]
checkNum = 2
sum = 0
# 유효 주민번호 판별
for index in range(len(inputNumList)-1):
    #sum += inputNumList[index] * checkNum[index]
    sum += inputNumList[index] * checkNum

    checkNum +=1
    if checkNum >=10:
        checkNum = 2
# 입력값 자리수(마지막 자리 제외) X 체크값 -> 합계

# 결과값 ->(11 - 합계값 % 11) % 10
result = 11 - (sum % 11) % 10
# 판별 결과 출력
# 결과값 == 주민번호 끝자리 값
if result == inputNumList[-1]:
    print("유효한 주민번호 입니다.")
else:
    print("유효하지 않은 주민번호 입니다.")
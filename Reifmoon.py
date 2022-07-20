'''
1이상의 양수 입력 아닐시 양수입력
짝수 홀수판별
3의배수, 7의 배수 판별
20000 입력시 종료

입력횟수 입력 값 출력

짝수,홀수 판별후 출력

3의 배수 판별 후 출력

7의 배수 판별 후 출력

'''




count = 1

while True:
    #키보드로 입력
    inputNumber = int(input("정수 값을 입력하세요"))
    #변수지정할때 단어 2개붙일경우 두번째단어는 대문자로 가독성좋음

    #입력값 예외처리 양의 정수만 허용
    if inputNumber <= 0:
        print("양의 정수를 입력하세요")
        continue

    #20000 이면 프로그램 종료

    if inputNumber == 20000:
        #종료
        break

    #입력 횟수와 입력 값 출력
    print(count, "번째 입력 : ",inputNumber)
    count +=1
    
    #짝수 또는 홀수 판별 후 출력
    if inputNumber % 2 == 0:
        print("\t\t짝수입니다.")
    else:
        print("\t\t홀수입니다.")

    if inputNumber % 3 == 0:
        print("\t\t3의배수입니다")

    if inputNumber % 7 == 0:
        print("\t\t7의배수입니다")
count_num=1
flag = True
while  flag:
    input_num = int(input(""))
    if input_num <=0:
        print("1이상 양수를 입력해주세요")
    else:
        if input_num == 20000:
            print("이용해주셔서 감사합니다")
            break
        print(count_num,"번째 입력 값은 =",input_num)
        if input_num % 2 == 1:
            print("\t""홀수입니다.")
        if input_num % 2 == 0:
            print("\t""짝수입니다.")
        if input_num % 3 == 0:
            print("\t""3의 배수입니다.")
        if input_num % 7 == 0:
            print("\t""7의 배수입니다.")
        
        count_num +=1
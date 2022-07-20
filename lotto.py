import random
while True:
     print("===================")
     print("        로또")
     print("1.자동")
     print("2.수동")
     print("3.프로그램종료")
     print("===================")
     #번호 입력받고 각자 알맞은 프로그램실행
     select_num = int(input("메뉴선택 : "))

     lot_grade = 0
     play_list=[]
     alist=[]
     #로또 번호생성
     for count in range(6):
          a = random.randint(1,45)
          #중복번호가 나올경우 다시 난수 입력받기
          while a in alist:
               a = random.randint(1,45)
          #리스트에 난수 넣기
          alist.append(a)
     if select_num == 1:
          for count in range(6):
               randnum= random.randint(1,45)
               while randnum in play_list:
                    randnum = random.randint(1,45)
               play_list.append(randnum)
          #로또번호랑 자동생성된 내 로또번호 비교
          for a in range(6):
                    if play_list[a] in alist:
                         lot_grade += 1

          print(alist)
          print(play_list)
          print("일치하는 숫자 개수는 : ",lot_grade)

     elif select_num == 2:
          lotCount=1
          #리스트에 추가한 번호가 6개가 될때까지 반복
          while lotCount <=6:
               picknum = int(input("번호를 골라주세요(1~45)"))
               #중복된 번호를 입력받았을경우
               if picknum in play_list:
                    print("중복입니다 다시골라주세요")
                    continue
               #입력받은수가 45보다 클경우
               if picknum > 45 or picknum<1:
                    print("1~45사이의 숫자만 입력해주세요")
                    continue
               play_list.append(picknum)
               lotCount += 1
          for a in range(6):
                    if play_list[a] in alist:
                         lot_grade += 1

          print(alist)
          print(play_list)
          print("일치하는 숫자 개수는 : ",lot_grade)

     elif select_num == 3:
          print("끝")
          break
     else:
          print("1~3번 메뉴중에서 골라주세요")
          continue
     
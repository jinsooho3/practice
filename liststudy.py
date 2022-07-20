#List: 자료 구조 (Data Structure)

#학생 다섯 명의 성적을 입력 받아 평균을 계산하시오.

#두개 이상의 자료를 하나로 묶어서 효율적으로 관리
#Composite Data Type : ->  Array & Linked list
#Abstract Data Type : -> List 

myList= []

# CRUD
#   - Create
#   - Read
#   - Update
#   - Delete

# "Create"
#   초기값
#myList= [3, 4, 5, 2.0, True, "Test"]

# append : 제일 마지막 원소 뒤에 추가
#myList.append(20)
# insert : 지정된 위치에 추가
#myList.insert(1, 80)

# "Read"
myList= [3, 4, 5, 2.0, True, "Test"]

#변수의 동작 모드는 두가지
#Get, Set
# test = 2
# print(test) <- Get Mode
# test= 3 <- Set Mode
#[ ] 연산자를 이용합니다.
print(myList[1])
myList[1] = 1000

#for문으로읽기

# "Update"
# myList[3] = 1000


# "Delete"
#
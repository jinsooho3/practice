#numbers라는 빈리스트 생성후 출력
numbers = []
print(numbers)
#append를 이용해서 numbers에 1,7,3,6,5,2,13,14를 순서대로 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
#그후 리스트 출력
print(numbers)
#numbers리스트의 원소들중 홀수는 모두 제거 그후 다시 리스트 출력
i=0
while i < (len(numbers)):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i +=1
print(numbers)
#numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입후 출력
numbers.insert(0, 20)
print(numbers)

#numbers 리스트를 정렬한 후 출력
numbers.sort()
print(numbers)
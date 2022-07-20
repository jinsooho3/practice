import random

alist =[]
for a in range(20):
    alist.append(random.randint(1,15))
blist =[1,2,3,4,5,6,7,8,9,10]
# 파이썬의 장점을 살린 퀵 정렬
def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1: return array
    
    pivot, tail = array[0], array[1:]
    
    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]
    
    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

quick_sort(blist)
print(quick_sort(blist))
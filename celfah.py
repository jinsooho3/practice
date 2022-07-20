#화씨를 섭씨로 바꾸는 함수 정의
def celtofah(fah):
    return(fah -32)*5/9
#화씨 리스트
temp_list=[40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트",temp_list)
#화씨리스트 원소 수만큼 반복
for repeat in range(len(temp_list)):
    #화씨리스트 원소 를 섭씨로 바꾸고 소수점 첫번째 자리에서 반올림
    #round(숫자, (소수점)자리수) 
    #자리수에 음수넣어서 정수부분도 반올림가능
    temp_list[repeat] =round(celtofah(temp_list[repeat]), 1)
print("섭씨 온도 리스트",temp_list)

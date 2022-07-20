#payment 에서 cost만큼을빼고
#남은금액에서 50000으로 나누고 몫만큼 곱하고 빼고
#다시 남은금액에서 10000으로 나누고 빼고 5000, 1000역시 같음
#동전금액은 그냥 표기
def calculate_change(payment, cost):
    fifty_count = (payment - cost)//50000
    ten_count = (payment -cost- fifty_count*50000)//10000
    five_count = (payment - cost- fifty_count*50000 - ten_count*10000)//5000
    one_count = (payment - cost - fifty_count*50000 - ten_count*10000 - five_count*5000)//1000
    print("50000원 지폐: ",fifty_count,"장")
    print("10000원 지폐: ",ten_count,"장")
    print("5000원 지폐: ",five_count,"장")
    print("1000원 지폐: ",ten_count,"장")
calculate_change(180000, 103000)

#quiz 3
a = 3
row = 5
while a !=0:
     value=0
     while value < row: #row 만큼 반복(세로줄)
          i = 0
          if a%2 == 0:
               while i < row: #row 만큼 반복(가로줄)
                    if value % 2 == 0:
                         print("*",end='')
                    else:
                         if i % 2 == 0:
                              print("*",end='')
                         else:
                              print(" ",end='')
                    i+=1

          else:
               while i < row:
                    if i == value:
                         print(" ",end='')
                    else:
                         print("*",end='')

                    i += 1
          value+=1
          print()
     a -=1
     print()
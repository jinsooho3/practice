a= 10 #int(input("숫자입력"))
for b in range(a*2-1):
     if b <= a-1:
          for c in range(a-b-1):
               print(" ",end='')
               
          for d in range(b*2+1):
               if d == 0 or d == b*2:
                    print("*",end='')
                    
               else:
                    print(" ",end='')
     else:          #b=a 일때부터
          for e in range(b-a+1):
               print(" ",end='')
               
          for f in range((a*2-b)*2-3):
               if f == 0 or f == ((a*2-b)*2-4):
                    print("*", end='')
               else:
                    print(" ",end='')
     print()
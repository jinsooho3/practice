#quiz 3

line = 5
a=2
for count in range(a):
     for value in range(line):
          if count % 2 == 0:
               for j in range(line):
                    if value % 2!=0 and count%2!=0:
                         print(" "," ",end='')
                    else:
                         print("*"," ",end='')

               print()
               
          else:
               for i in range(line):
                    if i == value:
                         print(" "," ",end='')
                    else:
                         print("*"," ",end= '')
               print()
     print()               
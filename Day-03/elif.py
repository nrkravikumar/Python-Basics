##elif:
##----
##      => three or more n number of cases
##      Syntax:
##      ---------
##            if (condition-1):
##                  //stmnt-1
##            elif (condition-2):
##                  //stmnt-2
##                  |             |
##            elif (condition-n):
##                  //stmnt-n
##            else:
##                  //stmnt-(n-2)
n = int(input("Enter a number: "))
if n>100:
      print(f"Entered number {n} is greater than 100")
elif n<70 and n>20:
      print(f"Entered number {n} is in between 70 and 20")
elif n>50:
      print(f"Entered number {n} is greater than 50")
else:
      print(f"Entered number {n}")

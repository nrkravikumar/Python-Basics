##Jumping Statements:
##--------------------------
##      - It exists or skips from a loop
##      - It should be used inside of  Loops[conditional]
##      - break
##      - continue
##      - pass
##      - return
##      

##break:
##      - It exists from a loop
##
##n = int(input("Enter a range: "))
##for i in range(1,n):
##      if i == 10:
##            break
##      else:
##            print(i,end=" ")

##Continue:
##      - It skips a present value
##      
##
##n = int(input("Enter a range: "))
##for i in range(1,n):
##      if i == 10 or i == 2 or i == 15:
##            continue
##      else:
##            print(i,end=" ")

##Pass:
##      - It skips a value but we can use for further implementation of a code

n = int(input("Enter a range: "))
for i in range(1,n):
      if i == 10:
            pass
      else:
            print(i,end=" ")

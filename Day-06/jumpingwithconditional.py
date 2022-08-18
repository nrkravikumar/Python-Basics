n = int(input("Enter a size: "))

##for i in range(1,n+1):
##      for j in range(1,n+1):
##            k = int(input("Enter a value: "))
##            if k%2==0:
##                  print(k)
##            else:
##                  break
##      print()

for i in range(1,n+1):
      for j in range(1,n+1):
            if i%2==0 or j%2==0:
                  continue
            else:
                  print("*",end=" ")
      print()

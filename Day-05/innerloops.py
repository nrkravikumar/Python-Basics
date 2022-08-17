##InnerLoops:
##      - Loop within a loop
##      - Alignments
##      - row => column
##n = int(input("Enter a row size: "))
##m = int(input("Enter a columns size: "))
##for i in range(1,n+1):
##      for j in range(1,m+1):
##            print(f"{i}{j}",end=" ")
##      print()

##n = int(input("Enter a range: "))
##for i in range(1,n+1):
##      for j in range(1,n-i+2):
##            print("*",end=" ")
##      print()

n = int(input("Enter a range: "))
for i in range(1,n+1):
      for j in range(1,n+1):
            if i==j or i+j == n+1:
                  print("*",end=" ")
            else:
                  print(" ",end=" ")
      print()

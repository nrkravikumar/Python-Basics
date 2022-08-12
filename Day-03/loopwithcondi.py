n = int(input("Enter a range:"))
##for i in range(n):
##      if i>5:
##            print(i,end=" ")
for i in range(n):
      if i>10:
            print(i,end="- ")
      elif i>5:
            print(i,end="$ ")
      elif i>3:
            print(i,end="* ")
      else:
            print(i,end="# ")

##while:
##-------
##      - For known and unknown ranges
##      Syntax:
##            initialization
##            while condition:
##                  //stmnts
##                  incr/decr

##i = 0
##n = int(input("enter a range: "))
##while i<n:
##      print(i,end=" ")
##      i+=1
##      

##n = int(input("Enter a range: "))
##while n>0:
##      n-=1
##      print(n,end=" ")

##i = 7
##n = int(input("enter a number: "))
##while i!=n:
##      print(n,end=" ")
##      n+=1

while True:
      print("1.Name\n2.Age\n3.Address\n4.Exit")
      n = int(input("Enter your choice: "))
      if n==1:
            name = input("Enter Your name: ")
            print(f"Your Name is: {name}")
      elif n==2:
            age = int(input("Enter Your age: "))
            print(f"Your age is: {age}")
      elif n==3:
            adr = input("Enter Your Location: ")
            print(f"Your Location is: {adr}")
      elif n == 4:
            break
      else:
            print("Enter a Valid Choice")

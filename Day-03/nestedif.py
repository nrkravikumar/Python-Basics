##Nested if:
##-----------
##      => Two or more cases
##      Syntax:
##      ----------
##            if (condition-1):
##                  if(condition-2):
##                        //stmnt-1
##                  else:
##                        //stmnt-2
##            else:
##                  //stmnt-3
usr = "sample"
pwd ="124"
##u = input("Enter username: ")
##p = input("Enter password: ")
##if u == usr:
##      if p == pwd:
##            print(f"Welcome User {u}!!!")
##      else:
##            print("Invalid Username or password")
##else:
##      print("Invalid Username or password")
us = input("Enter username: ")
if us == usr:
      ps = input(f"{us} Enter password: ")
      if ps == pwd:
            print(f"Welcome User {us}!!!")
      else:
            print("Invalid Password")
else:
      print(f"Invalid username {us}")

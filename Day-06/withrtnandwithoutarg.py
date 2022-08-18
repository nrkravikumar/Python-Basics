##=>With returntype and without arguments
##    => printing -> Main
##    => reading -> Function
##    => logic -> Function

def adtn():
      n = int(input("Enter a value: "))
      m = int(input("Enter b value: "))
      print(f"Addition of {n} and {m} is: ",end=" ")
      return n+m

print(f"{adtn()}")

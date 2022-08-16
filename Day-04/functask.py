vip = [('John',100),('Mary',200),('Peter',0)]
def printdollars(mn=20):
      print(f"${mn}")

for i in vip:
      na = input("Lei see, name? ")
      if i[0] == na:
            printdollars(i[1])
      elif na == "bye":
            print("Bye!")
            break
      else:
            printdollars()

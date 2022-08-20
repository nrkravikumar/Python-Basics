##default argument:
##      - variablename
##      - value fixed

def prntname(name='lalitha',age,year=2):
      print(f"Entered name is: {name}")
      print(f"Entered age is: {age}")
      print(f"Entered year is: {year}")
      return

n = input("Enter a name: ")
##a = input("Enter your age: ")
##y = input("Enter your year: ")
##prntname(n,a,y)
prntname(n)

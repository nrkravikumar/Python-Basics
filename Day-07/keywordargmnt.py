##Keyword arguments:
##      - keys same
##      - function arguments keys different positions
##      

def empdtls(esal2,ename,eage):
      print(f"Employee Name: {ename}")
      print(f"Employee Age: {eage}")
      print(f"Employee Salary: {esal}")
      return
      
en = input("Enter an Employee name: ")
ea = input("Enter an Emlpoyee age: ")
es = input("Enter an Employee salary: ")
empdtls(eage=ea,ename=en,esal=es)

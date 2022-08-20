##Variable Length argument:
##      - variable
##      - * => tuple
##      - ** => Dictionary
##      

def pr(name,*p):
      print(name,type(name))
      print(p,type(p))
      return

n = input("Enter a name: ")
pr(n,45,78,45,98,65,45,78,'tilak','45.00',False)

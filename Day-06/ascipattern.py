##n = input("Enter a character: ")
##print(n,ord(n))

##c = int(input("Enter a number: "))
##print(c,chr(c))

##for i in range(1,256):
##      print(f"{i} => {chr(i)}",end=" ")

n = int(input("Enter a size: "))

for i in range(1,n+1):
      for j in range(1,n+1):
            print(f"{chr(64+i)}{j}",end=" ")
      print()

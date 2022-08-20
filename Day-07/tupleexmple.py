b = (45,23.0125,'Lalitha',True,'78.012',45)
print(b,type(b))
##print(dir(tuple))
##print(b.count(4))
##print(b.index(True))
print(len(b))
for i in range(len(b)):
      if i == 3:
            continue
      else:
            print(b[i],end=" ")
print()
for i in b:
      if i == True:
            continue
      else:
            print(i,end=" ")

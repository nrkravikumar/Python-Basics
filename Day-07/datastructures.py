##Data Structures or Data types or Itertor or Repitior
##====================================
##      => To organize the data in order or unorder format
##      => List
##      => Tuple
##      => Set
##      => Dictionary
##      => String

##Tuple:
##      => It can be represented as "()"
##      => Values Cant be changed
##      => Slicing can be done because of index values
##      => It can be type casted as "tuple()"
##      => Values can be stored in order format
##      => Different data type values can be stored
##      => It allows duplicate values

f = (12,45.012,'Prasad',False,'78','89.052',12,12,12)
print(f,type(f))
print(f[0])
##print(dir(tuple))
print(f.count(12))
print(f.count(1))
print(f.index('Prasad'))
##print(f.index('Shyam')) // not in tuple
for i in range(len(f)):
      print(f[i],end=" ")
print()
for i in f:
      print(i,end=" ")

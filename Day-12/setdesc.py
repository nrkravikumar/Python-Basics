##Set:
##===
##      - It can be represented as "{}" but it contains any single character or data type value in it
##      - It cant allows duplicate value elements
##      - It stores the data in unorder format by using print statement order in kernel
##      - It can be typecasted as set()
##      - Slicing cant be done because of no index
##      - It can changes the value of items
##      

w = {}
print(w,type(w))
g = {'a'}
print(g,type(g))
c = {45,23.015,True,'Priya','45.0124',12,12,12}
c
print(dir(set))

print(c)
c.add(34)
print(c)
f = c.copy()
print(c,id(c))
print(f,id(f))
f.add(56)
print(c)
print(f)
c.pop()
print(c)
c.pop()
print(c)
##c.pop(23.015)
##print(c)
c.remove(23.015)
print(c)
c.remove(45)
print(c)
c.update({12,45,78})
print(c)
c.update([45,78,89,200])
print(c)




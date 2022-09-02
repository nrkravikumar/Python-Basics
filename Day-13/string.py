##String:
##=====
##      - It can be enclosed with ' or " or """ => comment
##      - It can stores all data type elements
##      - It can be typecasted as str()
##      - Slicing can be done because of index values
##      - It can changes the values and address of a string
##      

d = "Welcome to PYthon ProGramming"
print(d,type(d))
##print(d[-4])
##print(d,id(d))
##f = d[4:-7]
##print(f,id(f))
##print(d,id(d))
##d = d[6:-8]
##print(d,id(d))
print(d.capitalize())
print(d.casefold())
print(d.swapcase())
print(d.title())
print("--------")
print(d.count('e'))
print(d.split('e'))
print(d.rsplit('o'))
b = "     Ramu is Good at Teaching"
h = "Prasad is Good at Playing Cricket     "
print(b.strip())
print(b.lstrip())
print(h.rstrip())
print("--".join(b))
print(b.ljust(50))
print(h.rjust(50))
print(b.center(90))
print(b.zfill(60))
print(dir(str))

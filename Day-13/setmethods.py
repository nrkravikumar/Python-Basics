a = {12,78,95,68,4}
b = {12,4,500,76,120,300,400}
print(a)
print(b)
##print(dir(set))
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a.difference(b))
print(a)
print(b)
a.difference_update(b)
print(a)
print(b)
f = {23,56,3,78}
v = {1,5,6,3,23,85,49}
print(f)
print(v)
f.intersection_update(v)
print(f)
print(v)
d = {12,78,45,23,56,89}
n = {12,78,5,23,96,400,500,120}
print(d)
print(n)
d.symmetric_difference_update(n)
print(d)
print(n)
print(dir(set))
z = {90,56,78}
print(z)
z.discard(90)
print(z)
z.discard(-45)
print(z)

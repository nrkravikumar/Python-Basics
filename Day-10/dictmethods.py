k = {'name':['Prasad','Sireesha'],'empid':'EP101','sal':25000}
print(k,type(k))
print(k.keys())
print(k.values())
print(k.items())
print(k.get('name'))
print(k.get('name')[0])
print(k['sal'])

c = k.copy()
print(k)
print(c,type(c))

print(c)
print(c.pop('name'))
print(c)

print(c.popitem())
##print(c.popitem('empid'))
print(c)

print(c)
c['empid']= 'EP102'
print(c)
c.update({'empid':'EP103'})
print(c)
c.setdefault('adr')
print(c)
c.update({'adr':'VJW'})
print(c)
c.setdefault('mble',78)
print(c)
c.clear()
print(c)

z = {}
v = [12,78,89,90]
x = [2,5,9,7]
z = z.fromkeys(x)
for i in range(len(x)):
      z.update({x[i]:v[i]})
print(z)

s = {}
for i,j in zip(x,v):
      s[i]=j
print(s)

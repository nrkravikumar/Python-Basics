
##n,c = int(input("Enter a number: ")),0
##print(f"Given number is {n}",end=" ")
##while n!=0:
##      n = n//10
##      c = c+1
##print(f"and its digits count is: {c}")

##n,r = int(input("Enter a number: ")),0
##print(f"Given number is:{n}",end=" ")
##while n!=0:
##      k = n%10
##      r = r*10+k
##      n=n//10
##print(f"and its reverse is: {r}")

##n = int(input("Enter a number: "))
##while n!=0:
##      k = n%10
##      if k%2==0:
##            print(k,end=" ")
##      n = n//10

n,c,r,s = int(input("Enter a number: ")),0,0,' '
while n!=0:
      k = n%10
      if k%2==0:
            s=s+str(k)+" "
      r = r*10+k
      c = c+1
      n = n//10
print(f"Digit Count is: {c}")
print(f"Reverse Number  is: {r}")
print(f"Even umbers are: {s}")





def readlist(m):
      '''Reading of n numbers to a list'''
      w = []
      for i in range(m):
            d = int(input())
            w.append(d)
      return w

def duplist(k):
      '''Removing duplicate values in a list'''
      dp = []
      for i in k:
            if i not in dp:
                  dp.append(i)
            else:
                  continue
      return dp

def evenlist(y):
      print("Even numbers in a list are: ",end=" ")
      for i in y:
            if i%2==0:
                  print(i,end=" ")
      return

n = int(input())
c = readlist(n)
v = duplist(c)
print(f"List values are: {c}")
print(f"After Duplicate values removing are: {v}")
evenlist(v)

d = 1
for i in range(1,6):
      for j in range(1,8):
            if d >=32:
                  break
            else:
                  if j == 3:
                        print("| |",end=" ")
                  elif i == 2:
                        print("$$",end=" ")
                  elif d%2==0 and d%5==0:
                        print("##",end=" ")
                  elif d%2==0:
                        print("**",end=" ")
                  elif d>=15:
                        print("[ ]",end=" ")
                  else:
                        print("{ }",end=" ")
            d+=1
      print()

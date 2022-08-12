n = int(input("Enter starting range: "))
m = int(input("Enter ending range: "))
k = int(input("Enter step range: "))
for i in range(n,m,k):
      if i>10:
            print(f"21EM1A05{i}")
      else:
            print(f"20EM1A04{i:02}")

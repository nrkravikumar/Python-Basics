##21AK1A0425 => 2
##20AK1A0525 => 3
def prntyr(roll,year=1,cllge='CL'):
      print(f"Roll number is: {roll} and year is: {year} year and college name is: {cllge}")
      return

r = input("Enter your roll number: ")
h = r[:2]
if h == "21":
      prntyr(r,year=2)
elif h == "20":
      prntyr(r,year=3)
elif h == "19":
      prntyr(r,year=4)
else:
      prntyr(r)



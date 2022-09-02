contactlist = {}

def addcnt():
      n = input("Enter Contact Name: ")
      if n not in contactlist:
            m = input("Enter Contact Number: ")
            a = input("Enter Age: ")
            contactlist[n] = [m,a]
            print(f"{n} Contact is Added\n")
      else:
            print(f"{n} Already Exists in Contact List\n")
      return contactlist

def vwcntlist():
      print("Contact Lists are:")
      print("========================")
      for i in contactlist.items():
            print(f"{i[0]} => {i[1][0]} -> {i[1][1]}")
      print("========================")
      return

def ucntmble():
      n = input("Enter a Contact Name: ")
      if n in contactlist:
            m = input("Enter New Mobile Number: ")
            if m not in contactlist.get(n)[0]:
                  contactlist.get(n)[0] = m
                  print(f"{m} New Number Updated")
            else:
                  print(f"{m} same mobile number")
      else:
            print(f"{n} Contact Not in Contact List")
      return contactlist

def ucntg():
      m = input("Enter a Contact Name: ")
      if m in contactlist:
            a = input("Enter New Age: ")
            if a not in contactlist.get(m)[1]:
                  contactlist.get(m)[1] = a
                  print(f"{a} New Age updated")
            else:
                  print(f"{a} same age")
      else:
            print(f"{m} not in Contact List")
      return contactlist

def sngprviw():
      n = input("Enter a Contact Name: ")
      if n in contactlist:
            print(f"======= {n} Details =======")
            print(f"Contact Name: {n}")
            print(f"Mobile Number: {contactlist.get(n)[0]}")
            print(f"Age: {contactlist.get(n)[1]}")
      else:
            print(f"{n} Name Not in a List")
            print("=========================")
      return

def dluser():
      n = input("Enter a Contact name: ")
      if n in contactlist:
            contactlist.pop(n)
            print(f"{n} removed Successfully")
      else:
            print(f"{n} Contact Doesnt Exists")
      return contactlist

def dlallusr():
      contactlist.clear()
      print("Contact List is removed")
      return contactlist

while True:
      print("1.Add Contact\n2.View Contact list\n"
            "3.Update Contact of Mobile\n"
            "4.Update Contact of Age\n5.View Contact details\n"
            "6.Delete Contact\n7.Delete All\n8.Exit\n")
      op = int(input("Enter your option: "))
      if op == 1:
            addcnt()
      elif op == 2:
            vwcntlist()
      elif op == 3:
            ucntmble()
      elif op == 4:
            ucntg()
      elif op == 5:
            sngprviw()
      elif op == 6:
            dluser()
      elif op == 7:
            dlallusr()
      elif op == 8:
            print("Exiting App\n")
            break
      else:
            print("Enter Valid option\n")

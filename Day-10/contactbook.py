cnt = {}

##for i in range(2):
##      name = input("Enter Name: ")
##      if name not in cnt.keys():
##            mble = input("Enter Mobile number: ")
##            age = int(input("Enter Age: "))
##            cnt[name] = [mble,age]
##            print(f"{name} added to contact List")
##            print(cnt)
##      else:
##            print(f"Already {name} Exists")

while True:
      print("1.Add Contact\n2.Display Contacts\n"
            "3.Change Contact\n4.Exit\n")
      op = int(input("Enter Your Option: "))
      if op == 1:
            name = input("Enter Contact Name: ")
            if name not in cnt.keys():
                  mobile = input("Enter Mobile Number: ")
                  age = input("Enter Age: ")
                  cnt[name] = [mobile,age]
                  print(f"{name} is Added to Contact List")
            else:
                  print(f"{name} Already Exists in Contact List")
      elif op == 2:
            print("Contacts List are: ")
            print("================")
            print("Name Mobile Age")
            print("----------------------------")
            for i in cnt.items():
                  print(f"{i[0]} {i[1][0]} {i[1][1]}")
                  print("----------------------------")
            print("================")
      elif op == 3:
            n = input("Enter a Name to Modify: ")
            if n in cnt.keys():
                  while True:
                        print("1.Mobile\n2.Age\n3.Exit\n")
                        mb = int(input("Enter option to change:"))
                        if mb == 1:
                              k = input("Enter Mobile Number: ")
                              if k!=cnt[n][0]:
                                    cnt[n][0]=k
                                    print(f"{k} New Mobile Number Updated")
                              else:
                                    print(f"{k} Already Exists")
                        elif mb==2:
                              a = input("Enter age:")
                              if a!=cnt[n][1]:
                                    cnt[n][1]=a
                                    print(f"{a} New age Updated")
                              else:
                                    print(f"{a} Already Exists")
                        elif mb==3:
                              break
                        else:
                              print("Enter Your Valid Choice to Change")
            else:
                  print(f"{n} Doesnt Exists in Contact List")
      elif op == 4:
            break
      else:
            print("Choose Valid Options in a list")

##Loops - Repititions - Iterations:
##      - To repeat a statement for n number of times
##      - for => particular range [Known ranges]
##      - while => Unknown ranges, Known ranges

##For:
##-----
##      => Kown ranges
##      Syntax:
##            for iterationvariablename in range(start,stop,end):
##                  //stmnts
##                or
##            for iterationvariablename in iterator:
##                  //stmnts
##            Iterators => Repititors => Data Structures => Data Types => [list,tuple,set,string and dictionary]

##range():
##---------
##      range(stop):
##      - By defaut it starts with 0
##      - It ends with stop-1 value
##      - It increments with 1 value
##      Ex:
##            range(5)
##            0 1 2 3 4
##            
##      range(start,stop):
##      - It starts with exactly start value
##      - It stops with stop-1 value
##      - It increments with 1 value
##      Ex:
##            range(5,10)
##            5 6 7 8 9
##
##      range(start,stop,step):
##      - It starts with exactly with start value
##      - It stops with stop-1 value
##      - It increments/decrements with step value
##      Ex:
##            range(10,20,3)
##            10 13 16 19
##            range(10,20,5)
##            10 15

n = int(input("Enter a range: "))
for i in range(n):
      print(i)
      

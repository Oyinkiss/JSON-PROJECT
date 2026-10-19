bags=["gucci", "pranda", "visio"]
prices=[40,20,100]
for bag, price in zip(bags, prices):
    #print(bag, price)
 bums= [1,2,3,4,5]
 square=list(map(lambda x: x**2, bums))
 even=list(filter(lambda x: x%2 ==0, bums))
print(square)
print(even)

#import
import math
from math import sqrt
print(math,sqrt(36))
from math import exp 
print(exp(1))

#definemodule
try:
 a=int(input("Enter value"))
 b=int(input("Enter value"))
 c= b/a
 print(c)
except ZeroDivisionError:
  print ("Cannot be zero")
except ValueError:
  print("Invalid input")
else:
  print("No Error")
finally:
  print("Execution completed")

  #loops
for i in range(5):
  if i==3:
    continue
  if i==3:
    break
  if i==0:
    pass
  print(i)
  #NestedLoop
for i in range(1,4):
   for j in range(1,4):
      print(i , j,end=" ")
   print()

#Word i control the row and j control the position within the row
#where you place print() determine the output format
for i in range(3,0,-1):
   for j in range(1, i+1):
      print(j,end=" ")
   print()
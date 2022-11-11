list1=[]
n=int(input("Enter the number of 1st elemnts :"))
print ("Enter 1st list elements")
for i in range (n):
  x = int(input())
  list1.append(x)
list1.sort()  
print(list1)

list2=[]
n=int(input("Enter the number of 2nd elemnts :"))
print ("Enter 2nd list elements")
for i in range (n):
  x = int(input())
  list2.append(x)
list2.sort()  
print(list2)

if(len(list1) == len(list2)):
 print("Both lists are of same length")
else:
 print("Both lists aren't in same length")



tot1 = 0
for i in range (len(list1)):
  tot1 = tot1 + list1[i]

tot2 = 0
for i in range (len(list2)):
  tot2 = tot2 + list2[i]

if tot1 == tot2:
 print("List sums to same value")
else:
 print("List doesn't sums to same value")



common = any(check in list1 for check in list2)
if common:
  print("Lists have common elements")
else:
  print("List doesn't have common elements")

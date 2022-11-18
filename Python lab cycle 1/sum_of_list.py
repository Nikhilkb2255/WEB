list=[]
n=int(input("Enter the number of elemnts :"))
print ("Enter the list elements :")
for i in range (n):
  x = int(input())
  list.append(x)
s = sum(list)
print ("Sum is:")
print(s)
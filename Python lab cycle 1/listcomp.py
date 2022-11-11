list=[]
n=int(input("Enter the number of 1st elemnts :"))
print ("Enter 1st list elements")
for i in range (n):
  x = int(input())
  list.append(x)
list.sort()  
print(list)

x = [i for i in list if i > 0]
print(x)

y = [i*i for i in list]
print(y)

m=str(input("Enter the string :"))
def vowel(m):
  vowels=["A","a","E","e","I","i","O","o","U","u"]
  final = [i for i in string if i in vowels]
  print(lrn(final))
  print(final)

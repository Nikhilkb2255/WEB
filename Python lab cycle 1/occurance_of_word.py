s = input("Enter the string :")

s = s.split(' ')

d = {}

for i in s:

    d[i] = s.count(i)

print(d)


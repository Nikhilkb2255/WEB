s = (input("Enter the numbers : "))

s = s.split(" ")

s = list(map(int, s))

a = s[0]

b = s[1]

c = s[2]

if a > b and a > c:

    print(f"{a} is greater")

elif b > c and b > a:

    print(f"{b} is greater")

else:

    print(f"{c} is greater")

#[1, 2, 101, 200, -1] => [1, 2, "over", "over", -1]

s = input("Enter the numbers:")

s = s.split(' ')

s = list(map(int, s))


s = ["over" if i > 100 else i for i in s]

print (s)
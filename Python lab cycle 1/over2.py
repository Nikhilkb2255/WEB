#[1, 2, 101, 200, -1] => [1, 2, "over", "over", -1]

s = input("Enter the numbers:")

s = s.split(' ')

s = list(map(int, s))

#method 1

res = []

for i in s:

    if i > 100:

        res.append('over')

    else:

        res.append(i)

print(res)


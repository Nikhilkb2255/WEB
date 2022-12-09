def word(x):
	y = []
	for i in x:
		y.append(len(i))
	return max(y)
a = input("Enter a list of words : ")
a = a.split(" ")
n = word(a)
print("Length of the longest word : ",n)


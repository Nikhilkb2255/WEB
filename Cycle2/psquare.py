def psquare(c,d):
	s = []
	for i in range(c,d):
		k = [int(x) for x in str(i)]
		if k[0]%2 == 0 and k[1]%2 == 0 and k[2]%2 == 0 and k[3]%2 == 0:
			s.append(i)
	sui = []
	for i in s:
		for j in range(1, i//2+1):
			if i/j == j:
				sui.append(i)
	print(sui)

a = int(input("Enter the starting range :"))
b = int(input("Enter the ending range :"))
psquare(a,b)


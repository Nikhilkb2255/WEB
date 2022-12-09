def psquare():
	from math import sqrt
	for number in range(1000, 10000):
		s1, s2 = list(str(number)),''
		for i in s1:
			if int(i) % 2 != 0:
				s2 = ''
				break
			s2 += i
		if len(s2) == 4:
			if len(str(sqrt(int(s2))).split('.')[1]) == 1:
				print(s2)
psquare()

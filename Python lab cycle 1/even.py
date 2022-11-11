s = input("Enter the input :")

s = s.split(" ")

s = list(map(int, s))

for i  in s:
	
    if (i%2 == 0):
	    
        s.remove(i)

print ("List after removing EVEN numbers : ")

print (s)
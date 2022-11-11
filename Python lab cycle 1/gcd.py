a, b = int(input("Enter Number 1:")), int(input("Enter Number 1:"))

for i in range(max(a, b), 0, -1):

    if a % i == 0 and b % i == 0:

        print(f"GCD is {i}")

        break
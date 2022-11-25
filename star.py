def star(n):

    for i in range(1):

        for i in range(1, n+1):

            print(f"{'*' * i}")

        for i in range(n-1, 0, -1):

            print(f"{'*' * i}")

n = int(input("Enter Star Size : "))

star(n)
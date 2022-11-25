def star(n):

    for i in range(0,n):

        for i in range(0, i+1):

            print("* ",end=" ")

        print("\r")

    for i in range(0,n):

        for i in range(n, 0, -1):

            print("* ",end=" ")

        print("\r")
    
n = int(input("Enter Star Size : "))

star(n)
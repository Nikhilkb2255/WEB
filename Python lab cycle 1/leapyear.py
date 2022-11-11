start = int(input("Enter the starting year : "))
end = int(input("Enter the ending year : "))

while start < end:
            if start%4 == 0 and start%100 != 0:
                print(start)
            if start%100 ==0 and start%400 ==0:
                print(start)
            start += 1

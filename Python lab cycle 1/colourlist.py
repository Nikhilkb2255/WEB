list1 = input("Enter the 1st list :")

list1 = list1.split(",")

list2 = input("Enter the 2nd list :")

list2 = list2.split(",")

for i in list1:

    if i not in list2:

        print (i)
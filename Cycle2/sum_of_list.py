def sum_of_list(l):

    total = 0

    for i in l:

        total += i

    return total

l = list(map(int, input("Enter the elements : ").split()))

print(sum_of_list(l))
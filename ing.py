def string():

    d = input("Enter the string : ")

    res = ""

    if d[-3:] == "ing":

        res += d[:-3:]

        res += "ly"

        return res

    else:
    
        d += "ing"

        return d

print(string())
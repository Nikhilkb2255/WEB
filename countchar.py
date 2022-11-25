def count(s):

  d = {}

  for i in set(s):

    d[i] = s.count(i)

  return d

print(count("Nikhil"))
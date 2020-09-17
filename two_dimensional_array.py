a = [[12, 24, 8], [30, 47, 2], [15, 6, 9]]
c = []

b = 0
for index, value in enumerate(a):
   b += a[index][index]
c.append(b)
e = 0
for index, value in enumerate(a):
    e += a[index][len(a[index])- index - 1]
c.append(e)
print(c)





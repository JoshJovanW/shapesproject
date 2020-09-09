a = [6, 2, 3, 7]
for index, value in enumerate(a):
    for idx, number in enumerate(a):
        if number > a[index]:
            b = number
            a[idx] = a[index]
            a[index] = b
print(a)


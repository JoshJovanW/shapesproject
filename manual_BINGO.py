a = [[1,1,1], [1,2,1], [1,2,1]]
if a[0][0] == a[1][0] and a[1][0] == a[2][0]:
    print("BINGO!")#to the right from top
else:
    print("not bingo")

if a[0][0] == a[1][1] and a[1][1] == a[2][2]:
    print("BINGO!")#diagonal to bottom right
else:
    print("not bingo")


if a[0][0] == a[0][1] and a[0][1] == a[0][2]:
    print("BINGO!")#to the bottom left from top
else:
    print("not bingo")


if a[0][1] == a[1][1] and a[1][1] == a[2][1]:
    print("BINGO!")#to the bottom middle from the middle top
else:
    print("not bingo")


if a[0][2] == a[1][2] and a[1][2] == a[2][2]:
    print("BINGO!")#bottom right from top right
else:
    print("not bingo")


if a[0][1] == a[1][1] and a[1][1] == a[2][1]:
    print("BINGO!")#middle right from middle left
else:
    print("not bingo")

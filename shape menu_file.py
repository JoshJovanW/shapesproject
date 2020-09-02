n = str(input("please input the shape: "))

if n == "rectangle":
    print("please input lenght: ")

    L = int(input())

    print("please input height: ")

    H = int(input())

    for height in range(H):
        for lenght in range(L):
            print("*",end=" ")
        print()

elif n == "hollow rectangle":
    print("please input lenght: ")

    l = int(input())

    print("please input height: ")

    h = int(input())

    for height in range (h):
        for lenght in range (l):
            if height == 0 or height == h-1 or lenght == 0 or lenght == l-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

elif n == "triangle":
    print("please input rows: ")

    r = int(input())

    for rows in range(r):
        print("*" * rows)

elif n == "hollow triangle":
    print("please input rows: ")

    R = int(input())

    for Rows in range(R):
        for Columns in range(R):
            if Columns == 0 or Rows == R-1 or Rows == Columns:
                print("*", end="")
            else:
                print(" ", end="")
        print()

else: 
    print("This is not a valid shape")


print("This is a simple application which prints simple polygons such as triangle and quadrilaterals and their hollow form as well.")

print()

def run():
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
        print("Sorry, but this is not a valid shape. Please try other shapes.")

print("Do you want to print a shape?")

a = str(input())

if a == "yes":
    print("available shapes: ")
    print()
    print("- rectangle ")
    print()
    print("- hollow rectangle ")
    print()
    print("- triangle ")
    print()
    print("- hollow triangle ")
    print()
    print("to print a shape write the name as shown above ")
    run()
else:
    print("have a good day :)")




if a == "yes":
    print("do you want to continue? type yes to continue.")

    ans = str(input())

    while ans == "yes":
        run()
        break
    else: 
        print("thank you for using this application:)")
else:
    print("thank you for using this application")

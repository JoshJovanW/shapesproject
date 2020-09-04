print("This is an application for arranging your list ")
print()
print("To use this application write a list of random numbers like below")
print()
print("90 2 17 23")
print()
print("Do you want to use this application? Type YES to use")
ans = str(input())
if ans == "YES":
    print ("write your list of numbers: ")

    numbers = [int(x) for x in input().split()]

    print (numbers)

    print("This is your list arranged")
    a = sorted(numbers)
    print(a)
else: 
    print("have a good day")

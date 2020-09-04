print("This is a minimal number finder")
print()
print("To use this application write a list of numbers as shown below")
print()
print("2 3 4 5 ")
print()
print("Do you want to use this application? Type YES to use")
ans = str(input())
if ans == "YES":
    print ("write your list of numbers: ")

    numbers = [int(x) for x in input().split()]

    print (numbers)

    print("This is the smallest number in your list: ")
    a = min(numbers)
    print(a)
    print("This is the biggest number in your list: ")
    b = max(numbers)
    print(b)
else: 
    print("have a good day")

n = int (input("please input the number of rows: "))

h = int(input("please input the number of columns: "))

for i in range(n):#n is always fized while i goes up the chain of n 
    for j in range(h):
        print(" " * (h-j), "*" * (n))
    print()
    break

a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def top_left():
    a[0][0] = int(input())

def top_middle():
    a[0][1] = int(input())

def top_right():
    a[0][2] = int(input())

def middle_left():
    a[1][0] = int(input())

def middle_middle():
    a[1][1] = int(input())

def middle_right():
    a[1][2] = int(input())

def bottom_left():
    a[2][0] = int(input())

def bottom_middle():
    a[2][1] = int(input())

def bottom_right():
    a[2][2] = int(input())

def play():
    print()
    print("to play this game you need two players.")
    print()
    print("write in X and O form (DO NOT WRITE IN ANY OTHER FORM OR THIS APP WILL NOT WORK)" )
    print()
    print("Player 1 = X")
    print()
    print("Player 2 = O")
    print()

def steps():
    print("to input your X or your O write the specific location on the 3x3 array")
    print()
    print("for example: middle_left or top_right. Don't forget to use the underscores")
    
    


print("This application is a console version of the BINGO! game. type yes to continue")

if input() == "yes":
    play()
else:
    print("Have a Good Day")

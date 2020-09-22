a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
def top_left():
    a[0][0] = sym

def top_middle():
    a[0][1] = sym

def top_right():
    a[0][2] = sym

def middle_left():
    a[1][0] = sym

def middle_middle():
    a[1][1] = sym

def middle_right():
    a[1][2] = sym

def bottom_left():
    a[2][0] = sym

def bottom_middle():
    a[2][1] = sym

def bottom_right():
    a[2][2] = sym

def not_valid():
    print("sorry this location is not valid")

def how_to_play():
    
    print()
    
    print("to play this game you need two players.")
    
    print()
    
    print("write in X and O form (DO NOT WRITE IN ANY OTHER FORM OR THIS APP WILL NOT WORK)" )
    
    print()
    
    print("Player 1 = X")
    
    print()
    
    print("Player 2 = O")
    
    print()
    
    print("to input your X or your O write the specific location on the 3x3 array")
    
    print()
    
    print("for example: middle_left or top_right. Don't forget to use the underscores")
    
    print()
    
    print("to input your symbol and location use this format. symbol, location for example: X top_right")
    
    print()
    sym, loc = input("enter your symbol and location like the format above: ").split()

def main():  
    if loc == "top_left":
        top_left() 

    elif loc == "top_middle":
        top_middle()

    elif loc == "top_right":
        top_right()
    
    elif loc == "middle_left":
        middle_left()
    
    elif loc == "middle_middle":
        middle_middle()
    
    elif loc == "middle_right":
        middle_right() 
    
    elif loc == "bottom_left":
        bottom_left() 

    elif loc == "bottom_middle":
        bottom_middle() 
  
    elif loc == "bottom_right":
        bottom_right() 
    
    else: 
        not_valid()
    
    print(a)

def top_left():
    a[0][0] = sym

def top_middle():
    a[0][1] = sym

def top_right():
    a[0][2] = sym

def middle_left():
    a[1][0] = sym

def middle_middle():
    a[1][1] = sym

def middle_right():
    a[1][2] = sym

def bottom_left():
    a[2][0] = sym

def bottom_middle():
    a[2][1] = sym

def bottom_right():
    a[2][2] = sym

def not_valid():
    print("sorry this location is not valid")




    


print("This application is a console version of the BINGO! game. type yes to continue")

if input() == "yes":
    how_to_play()
    main()
else:
    print("Have a Good Day")

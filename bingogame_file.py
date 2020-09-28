a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# player a 
def top_Left_A():
    a[0][0] = "x"

def top_Middle_A():
    a[0][1] = "x"

def top_Right_A():
    a[0][2] = "x"

def middle_Left_A():
    a[1][0] = "x"

def middle_Middle_A():
    a[1][1] = "x"

def middle_Right_A():
    a[1][2] = "x"

def bottom_Left_A():
    a[2][0] = "x"

def bottom_Middle_A():
    a[2][1] = "x"

def bottom_Right_A():
    a[2][2] = "x"

def not_Valid_A():
    print("sorry this location is not valid")

#player b 

def top_Left_B():
    a[0][0] = "O"

def top_Middle_B():
    a[0][1] = "O"

def top_Right_B():
    a[0][2] = "O"

def middle_Left_B():
    a[1][0] = "O"

def middle_Middle_B():
    a[1][1] = "O"

def middle_Right_B():
    a[1][2] = "O"

def bottom_Left_B():
    a[2][0] = "O"

def bottom_Middle_B():
    a[2][1] = "O"

def bottom_Right_B():
    a[2][2] = "O"

def not_Valid_B():
    print("sorry this location is not valid")




def how_to_play():
    
    "This is a sentence.\n"
    
    print("to play this game you need two players.")
    
    "This is a sentence.\n"
    
    print("write in X and O form (DO NOT WRITE IN ANY OTHER FORM OR THIS APP WILL NOT WORK)" )
    
    "This is a sentence.\n"
    
    print("Player 1 = X")
    
    "This is a sentence.\n"
    
    print("Player 2 = O")
    
    "This is a sentence.\n"
    
    print("to input your X or your O write the specific location on the 3x3 array")
    
    "This is a sentence.\n"
    
    print("for example: middle_left or top_right. Don't forget to use the underscores")
    
    "This is a sentence.\n"

    
    
    

def main_A():  
   print("start with player A. Enter your location.")

    if input() == "top_left":
        top_left() 

    elif input() == "top_middle":
        top_middle()

    elif input() == "top_right":
        top_right()
    
    elif input() == "middle_left":
        middle_left()
    
    elif input() == "middle_middle":
        middle_middle()
    
    elif input() == "middle_right":
        middle_right() 
    
    elif input() == "bottom_left":
        bottom_left() 

    elif input() == "bottom_middle":
        bottom_middle() 
  
    elif input() == "bottom_right":
        bottom_right() 
    
    else: 
        not_valid()
    
    print(a)

def main_B():  
   print("Player B's turn. Enter your location.")

    if input() == "top_left":
        top_left() 

    elif input() == "top_middle":
        top_middle()

    elif input() == "top_right":
        top_right()
    
    elif input() == "middle_left":
        middle_left()
    
    elif input() == "middle_middle":
        middle_middle()
    
    elif input() == "middle_right":
        middle_right() 
    
    elif input() == "bottom_left":
        bottom_left() 

    elif input() == "bottom_middle":
        bottom_middle() 
  
    elif input() == "bottom_right":
        bottom_right() 
    
    else: 
        not_valid()
    
    print(a)



print("This application is a console version of the BINGO! game. type yes to continue")

if input() == "yes":
    how_to_play()
    main()
else:
    print("Have a Good Day")

a = [[" "," "," "], [" "," "," "], [" "," "," "]]

def how_to_play():
    print("This application is a console version of the BINGO! game.\n")

    print("to play this game you need two players.\n")
    
    print("Player 1 = X \n")
    
    print("Player 2 = O \n")
    
    print("to input your X or your 0 write the specific location on the 3x3 array \n")
    
    print("for example: middle_left or top_right. Don't forget to use the underscores \n")
    
# assigning variable

def top_Left(shape):
    if a[0][0] == " ":
        a[0][0] = shape
        next_Turn()
        
    
def top_Middle(shape):
    if a[0][1] == " ":
        a[0][1] = shape
        next_Turn()
        
    
def top_Right(shape):
    if a[0][2] == " ":
        a[0][2] = shape
        next_Turn()
        
   
def middle_Left(shape):
    if a[1][0] == " ":
        a[1][0] = shape
        next_Turn()
        

def middle_Middle(shape):
    if a[1][1] == " ":
        a[1][1] = shape
        next_Turn()
        

def middle_Right(shape):
    if a[1][2] == " ":
        a[1][2] = shape
        next_Turn()
        

def bottom_Left(shape):
    if a[2][0] == " ":
        a[2][0] = shape
        next_Turn()
       

def bottom_Middle(shape):
    if a[2][1] == " ":
        a[2][1] = shape
        next_Turn()        

def bottom_Right(shape):
    if a[2][2] == " ":
        a[2][2] = shape
        next_Turn()
       

def not_Valid():
    print("sorry this location is not valid")


#identification 

def player_A():
    print("Player a's Turn.\n")

def player_B():
    print("Player b's Turn.\n")

def ask_For_Input():
    print("please input your location. write in this form ('top left')")


#main logic 

def main():
    if location == "top left":
        top_Left(shape) 

    elif location == "top middle":
        top_Middle(shape)

    elif location == "top right":
        top_Right(shape)
    
    elif location == "middle left":
        middle_Left(shape)
    
    elif location == "middle middle":
        middle_Middle(shape)
    
    elif location == "middle right":
        middle_Right(shape) 
    
    elif location == "bottom left":
        bottom_Left(shape) 

    elif location == "bottom middle":
        bottom_Middle(shape) 
  
    elif location == "bottom right":
        bottom_Right(shape) 
    
    else: 
        not_Valid()

#bingo checking

def top_Right_From_Top(shape_bingo):
    return a[0][0] == shape_bingo and a[0][1] == shape_bingo and a[0][2] == shape_bingo
    # to the right from top


def diagonal_To_Bottom_Right(shape_bingo):
    return a[0][0] == shape_bingo and a[1][1] == shape_bingo and a[2][2] == shape_bingo    
    # diagonal to bottom right


def bottom_Left_From_Top(shape_bingo):
    return a[0][0] == shape_bingo and a[1][0] == shape_bingo and a[2][0] == shape_bingo      
    # to the bottom left from top


def bottom_Middle_From_Mid_Top(shape_bingo):
    return a[0][1] == shape_bingo and a[1][1] == shape_bingo and a[2][1] == shape_bingo       
    # to the bottom middle from the middle top


def bottom_Right_From_Top_Right(shape_bingo):
    return a[0][2] == shape_bingo and a[1][2] == shape_bingo and a[2][2] == shape_bingo        
    # bottom right from top right


def middle_Left_From_Right(shape_bingo):
    return a[1][0] == shape_bingo and a[1][1] == shape_bingo and a[1][2] == shape_bingo       
    # middle left from middle right


def bottom_Left_To_Bottom_Right(shape_bingo):
    return a[2][0] == shape_bingo and a[2][1] == shape_bingo and a[2][2] == shape_bingo       
    # bottom left to bottom right


def bottom_Left_From_Top(shape_bingo):
    return a[2][0] == shape_bingo and a[1][1] == shape_bingo and a[0][2] == shape_bingo      
    # bottom left to top right

# printing bingo 

def checker_A():
    if top_Right_From_Top(shape_bingo):
        Bingo_A()
        bingo_Found()
        
        

    elif diagonal_To_Bottom_Right(shape_bingo):
        Bingo_A()
        bingo_Found()
        
        

    elif bottom_Left_From_Top(shape_bingo):
        Bingo_A()
        bingo_Found()
        

    elif bottom_Middle_From_Mid_Top(shape_bingo):
        Bingo_A()
        bingo_Found()
        

    elif bottom_Right_From_Top_Right(shape_bingo):
        Bingo_A()
        bingo_Found()
        

    elif middle_Left_From_Right(shape_bingo):
        Bingo_A()
        bingo_Found()
        

    elif bottom_Left_To_Bottom_Right(shape_bingo):
        Bingo_A()
        bingo_Found()
        

    elif bottom_Left_From_Top(shape_bingo):
        Bingo_A()
        bingo_Found()
        
    



def checker_B():
    if top_Right_From_Top(shape_bingo):
        Bingo_B()
        bingo_Found()
        

    elif diagonal_To_Bottom_Right(shape_bingo):
        Bingo_B()
        bingo_Found()
        

    elif bottom_Left_From_Top(shape_bingo):
        Bingo_B()
        bingo_Found()
        

    elif bottom_Middle_From_Mid_Top(shape_bingo):
        Bingo_B()
        bingo_Found()
        

    elif bottom_Right_From_Top_Right(shape_bingo):
        Bingo_B()
        bingo_Found()
        

    elif middle_Left_From_Right(shape_bingo):
        Bingo_B()
        bingo_Found()
        

    elif bottom_Left_To_Bottom_Right(shape_bingo):
        Bingo_B()
        bingo_Found()
        

    elif bottom_Left_From_Top(shape_bingo):
        Bingo_B()
        bingo_Found()
        

def next_Turn():
    global loc
    loc = "added"

def bingo_Found():
    global bingo
    bingo = "found"

def shape_A():
    global shape 
    shape = "x"

def shape_Bingo_A():
    global shape_bingo
    shape_bingo = "x"

def shape_B():
    global shape
    shape = "O"

def shape_Bingo_B():
    global shape_bingo
    shape_bingo = "O"

def Bingo_A():
    print("BINGO! Player A wins!")

def Bingo_B():
    print("BINGO! Player B wins!")


bingo = "not found"

loc = "not added to"

how_to_play()

while bingo == "not found":
    if loc == "not added to":
        player_A()

        shape_A()

        shape_Bingo_A()

        ask_For_Input()

        location = input()

        main()
    checker_A()
    loc = "not added to"

    if loc == "not added to":
        player_B()

        shape_B()

        shape_Bingo_B()

        ask_For_Input()

        location = input()

        main()
    checker_B()
    print(a)
    loc = "not added to"

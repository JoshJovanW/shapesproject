a = [[1, 1, 1], [1, 2, 1], [1, 2, 1]]

def Top_Right_From_Top():
    if a[0][0] == a[0][1] and a[0][1] == a[0][2]:
        return True

    # to the right from top


def Diagonal_To_Bottom_Right():
    if a[0][0] == a[1][1] and a[1][1] == a[2][2]:
        return True
    # diagonal to bottom right


def Bottom_Left_From_Top():
    if a[0][0] == a[1][0] and a[1][0] == a[2][0]:
        return True
    # to the bottom left from top


def Bottom_Middle_From_Mid_Top():
    if a[0][1] == a[1][1] and a[1][1] == a[2][1]:
        return True
    # to the bottom middle from the middle top


def Bottom_Right_From_Top_Right():
    if a[0][2] == a[1][2] and a[1][2] == a[2][2]:
        return True
    # bottom right from top right


def Middle_Left_From_Right():
    a[1][0] == a[1][1] and a[1][1] == a[1][2]
    # middle left from middle right


def Bottom_Left_To_Bottom_Right():
    a[2][0] == a[2][1] and a[2][1] == a[2][2]
    # bottom left to bottom right


def Bottom_Left_From_Top():
    a[2][0] == a[1][1] and a[1][1] == a[0][2]
    # bottom left to top right


def Last_Resort():
    print("NOT BINGO!")


def Bingo():
    print("BINGO!")


if Top_Right_From_Top():
    Bingo()

elif Diagonal_To_Bottom_Right():
    Bingo()

elif Bottom_Left_From_Top():
    Bingo()

elif Bottom_Middle_From_Mid_Top():
    Bingo()

elif Bottom_Right_From_Top_Right():
    Bingo()

elif Middle_Left_From_Right():
    Bingo()

elif Bottom_Left_To_Bottom_Right():
    Bingo()

elif Bottom_Left_From_Top():
    Bingo()

else: 
    Last_Resort()


   

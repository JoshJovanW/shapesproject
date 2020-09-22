a = [[1, 1, 1], [1, 2, 1], [1, 2, 1]]

# a = [[1, 2 ,1], [1, 2, 1], [1, 2, 1]]

# a = [[1, 2 ,1], [4, 1, 5], [5, 4, 1]]

# a = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]

def top_right_from_top():
    if a[0][0] == a[0][1] and a[0][1] == a[0][2]:
        return True

    # to the right from top


def diagonal_to_bottom_right():
    if a[0][0] == a[1][1] and a[1][1] == a[2][2]:
        return True
    # diagonal to bottom right


def bottom_left_from_top():
    if a[0][0] == a[1][0] and a[1][0] == a[2][0]:
        return True
    # to the bottom left from top


def bottom_middle_from_mid_top():
    if a[0][1] == a[1][1] and a[1][1] == a[2][1]:
        return True
    # to the bottom middle from the middle top


def bottom_right_from_top_right():
    if a[0][2] == a[1][2] and a[1][2] == a[2][2]:
        return True
    # bottom right from top right


def middle_left_from_right():
    a[1][0] == a[1][1] and a[1][1] == a[1][2]
    # middle left from middle right


def bottom_left_to_bottom_right():
    a[2][0] == a[2][1] and a[2][1] == a[2][2]
    # bottom left to bottom right


def bottom_left_from_top():
    a[2][0] == a[1][1] and a[1][1] == a[0][2]
    # bottom left to top right


def last_resort():
    print("NOT BINGO!")


def Bingo():
    print("BINGO!")


if top_right_from_top():
    Bingo()

elif diagonal_to_bottom_right():
    Bingo()

elif bottom_left_from_top():
    Bingo()

elif bottom_middle_from_mid_top():
    Bingo()

elif bottom_right_from_top_right():
    Bingo()

elif middle_left_from_right():
    Bingo()

elif bottom_left_to_bottom_right():
    Bingo()

elif bottom_left_from_top():
    Bingo()

else: 
    last_resort()

   

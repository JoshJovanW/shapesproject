a = [[1, 1, 1], [1, 2, 1], [1, 2, 1]]
print("Find BINGO?")


def TopRightFromTop():
    a[0][0] == a[0][1] and a[0][1] == a[0][2]
    # to the right from top


def DiagonalToBottomRight():
    a[0][0] == a[1][1] and a[1][1] == a[2][2]
    # diagonal to bottom right


def BottomLeftFromTop():
    a[0][0] == a[1][0] and a[1][0] == a[2][0]
    # to the bottom left from top


def BottomMiddleFromMidTop():
    a[0][1] == a[1][1] and a[1][1] == a[2][1]
    # to the bottom middle from the middle top


def BottomRightFromTopRight():
    a[0][2] == a[1][2] and a[1][2] == a[2][2]
    # bottom right from top right


def MiddleLeftFromRight():
    a[1][0] == a[1][1] and a[1][1] == a[1][2]
    # middle left from middle right


def BottomLeftToBottomRight():
    a[2][0] == a[2][1] and a[2][1] == a[2][2]
    # bottom left to bottom right


def BottomLeftFromTop():
    a[2][0] == a[1][1] and a[1][1] == a[0][2]
    # bottom left to top right


def LastResort():
    print("NOT BINGO!")


def Bingo():
    print("BINGO!")


if input() == "yes":

    if TopRightFromTop():
      return Bingo()

    elif DiagonalToBottomRight():
        return Bingo()

    elif BottomLeftFromTop():
        return Bingo()

    elif BottomMiddleFromMidTop():
        return Bingo()

    elif BottomRightFromTopRight():
        return Bingo()

    elif MiddleLeftFromRight():
        return Bingo()

    elif BottomLeftToBottomRight():
        return Bingo()

    elif BottomLeftFromTop():
        return Bingo()

else:
    return LastResort()

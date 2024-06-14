def Board(x_input, o_input):

    zero = 'X' if x_input[0] else ('O' if o_input[0] else 0)
    one = 'X' if x_input[1] else ('O' if o_input[1] else 1)
    two = 'X' if x_input[2] else ('O' if o_input[2] else 2)
    three = 'X' if x_input[3] else ('O' if o_input[3] else 3)
    four = 'X' if x_input[4] else ('O' if o_input[4] else 4)
    five = 'X' if x_input[5] else ('O' if o_input[5] else 5)
    six = 'X' if x_input[6] else ('O' if o_input[6] else 6)
    seven = 'X' if x_input[7] else ('O' if o_input[7] else 7)
    eight = 'X' if x_input[8] else ('O' if o_input[8] else 8)

    print(f"{zero}| {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven}| {eight}")


def CheckWin(x_input,o_input):

    wins = [[0,1,2],[1,4,7],[2,5,8],[0,3,6],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]

    for win in wins:
        if(x_input[win[0]]+x_input[win[1]]+x_input[win[2]]==3):
            return 1
            print("X wins")
        if(o_input[win[0]]+o_input[win[1]]+o_input[win[2]]==3):
            return 0
            print("O wins")
    return -1


x_input = [0,0,0,0,0,0,0,0,0]
o_input = [0,0,0,0,0,0,0,0,0]
turn = 1

print()

while(True):
    Board(x_input,o_input)
    
    if(turn == 1):
        value = int(input("X's turn: "))
        x_input[value] = 1
    else:
        value = int(input("O's turn: "))
        o_input[value] = 1
    

    cwin = CheckWin(x_input, o_input)
    if(cwin!=-1):
        print("Game Over")
        break
    turn = 1 - turn






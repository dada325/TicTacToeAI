# write your code here

def print_board(matrix):
    print("---------")
    print("| {} {} {} |".format(matrix[0][0], matrix[0][1], matrix[0][2]))
    print("| {} {} {} |".format(matrix[1][0], matrix[1][1], matrix[1][2]))
    print("| {} {} {} |".format(matrix[2][0], matrix[2][1], matrix[2][2]))
    print("---------")


def next_move():
    print("Enter the coordinates: ")
    coordinate = list((input().split(" ")))
    return coordinate


def is_not_occupied(move, matrix):
    if matrix[move[0]-1][move[1]-1] == " " or matrix[move[0]-1][move[1]-1] == "_":
        return True
    else:
        return False


def is_number(move):
    result = 1
    for i in range(0, len(move)):
        if move[i].isdigit():
            result *= 1
        else:
            result *= 0
    return result


def is_in_range(move):
    if 0 <= int(move[0]-1) < 3 and 0 <= int(move[1]-1) < 3:
        return True
    else:
        return False


def make_the_move(matrix):
    global state
    while True:
        move = next_move()
        if is_number(move):
            for i in range(0, len(move)):
                move[i] = int(move[i])
            if is_in_range(move):
                if is_not_occupied(move, matrix):
                    if abs(count_o()-count_x()) == 0:
                        matrix[move[0] - 1][move[1] - 1] = "X"
                    else :
                        matrix[move[0] - 1][move[1] - 1] = "O"
                    outcome = [matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][0], matrix[1][1], matrix[1][2], matrix[2][0], matrix[2][1], matrix[2][2]]
                    join_outcome = "".join(outcome)
                    state = join_outcome
                    print_board(matrix)
                    break
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


def count_x():
    sum_of_x = 0
    for i in range(0,len(state)):
        if state[i] == "X":
            sum_of_x += 1
    return sum_of_x


def count_o():
    sum_of_o = 0
    for i in range(0,len(state)):
        if state[i] == "O":
            sum_of_o += 1
    return sum_of_o


def count_space():
    sum_of_space = 0
    for i in range(0, len(state)):
        if state[i] == "_" or state[i] == " ":
            sum_of_space += 1
    return sum_of_space

def x_win():
    horizontal_win = 0
    vertical_win = 0
    diagonal_win = 0
    if matrix[0][0] == "X" and matrix[0][1] == "X" and matrix[0][2] == "X" or matrix[1][0] == "X" and matrix[1][1] == "X" and matrix[1][2] == "X" or matrix[2][0] == "X" and matrix[2][1] == "X" and matrix[2][2] == "X":
        horizontal_win = 1
    if matrix[0][0] == "X" and matrix[1][0] == "X" and matrix[2][0] == "X" or matrix[0][1] == "X" and matrix[1][1] == "X" and matrix[2][1] == "X" or matrix[0][2] == "X" and matrix[1][2] == "X" and matrix[2][2] == "X":
        vertical_win = 1
    if matrix[0][0] == "X" and matrix[1][1] == "X" and matrix[2][2] == "X" or matrix[0][2] == "X" and matrix[1][1] == "X" and matrix[2][0] == "X":
        diagonal_win = 1

    return horizontal_win or vertical_win or diagonal_win


def o_win():
    horizontal_win = 0
    vertical_win = 0
    diagonal_win = 0
    if matrix[0][0] == "O" and matrix[0][1] == "O" and matrix[0][2] == "O" or matrix[1][0] == "O" and matrix[1][
        1] == "O" and matrix[1][2] == "O" or matrix[2][0] == "O" and matrix[2][1] == "O" and matrix[2][2] == "O":
        horizontal_win = 1
    if matrix[0][0] == "O" and matrix[1][0] == "O" and matrix[2][0] == "O" or matrix[0][1] == "O" and matrix[1][
        1] == "O" and matrix[2][1] == "O" or matrix[0][2] == "O" and matrix[1][2] == "O" and matrix[2][2] == "O":
        vertical_win = 1
    if matrix[0][0] == "O" and matrix[1][1] == "O" and matrix[2][2] == "O" or matrix[0][2] == "O" and matrix[1][
        1] == "O" and matrix[2][0] == "O":
        diagonal_win = 1

    return horizontal_win or vertical_win or diagonal_win


def display_state():
    x = count_x()
    o = count_o()
    space = count_space()
    difference = abs(x - o)
    both_win = 1 if x_win()*o_win() == 1 else 0
    if difference < 2 and not both_win:
        if x_win():
            print("X wins")
        elif o_win():
            print("O wins")
        elif space == 0:
            print("Draw")
        else:
            print("Game not finished")

    else:
        print("State is not possible")


print("Enter the cells:")
state = input()
m = 3
n = 3
matrix = [[" " for x in range(n)] for x in range(m)]
matrix[0][0] = state[0]
matrix[0][1] = state[1]
matrix[0][2] = state[2]
matrix[1][0] = state[3]
matrix[1][1] = state[4]
matrix[1][2] = state[5]
matrix[2][0] = state[6]
matrix[2][1] = state[7]
matrix[2][2] = state[8]

print_board(matrix)
make_the_move(matrix)
display_state()

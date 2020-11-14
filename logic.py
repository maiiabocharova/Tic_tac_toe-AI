import copy
from math import inf
WINNER_POSITIONS = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                    {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
                    {0, 4, 8}, {2, 4, 6})

board = list(» " * 9)
def player(board):
    if board.count(«X») ≤ board.count(«O»):
        return «X»
    else:
        return «O»
def convert_coordinates(coord_x, coord_y):
    return (coord_x — 1) + (3 * (3 — coord_y))
def win(board):
    global winner
    current_pos = {i for i in range(9) if board[i] == «X"}
    for winner_pos in WINNER_POSITIONS:
        if current_pos.issuperset(winner_pos):
            winner = «X»
            return «X»
    current_pos = {i for i in range(9) if board[i] == «O"}
    for winner_pos in WINNER_POSITIONS:
        if current_pos.issuperset(winner_pos):
            winner = «O»
            return «O»
    else:
        return None

def empty_cells(board):
    cells = []
    for i in range(9):
        if board[i] == " «:
            cells.append(i)
    return cells

def set_move(move):
    board[move] = player(board)
def update_field(move):
    board[move] = player(board)
def terminal(board):
    if win(board) is not None or board.count(» «) == 0:
        return True
    return False
def print_field():
    print(9 * «-»)
    for row in range(3):
        print(«|», " «.join(board[row * 3: 3 + row * 3]), «|»)
    print(9 * «-»)
def utility(board):
    if terminal(board):
        if win(board) == «X»:
            return 1
        elif win(board) == «O»:
            return -1
        else:
            return 0
def result(board, action):
    result = copy.deepcopy(board)
    result[action] = player(board)
    return result

def minimax(board):
    if terminal(board):
        return None
    if player(board) == «X»:
        best_v = -inf
        for move in empty_cells(board):
            max_v = min_value(result(board, move))
            if max_v > best_v:
                best_v = max_v
                best_move = move
    elif player(board) == «O»:
        best_v = +inf
        best_move = None
        for move in empty_cells(board):
            min_v = max_value(result(board, move))
            if min_v < best_v:
                best_v = min_v
                best_move = move
    return best_move
def max_value(board):
    if terminal(board):
        return utility(board)
    else:
        v = -inf
        for move in empty_cells(board):
            v = max(v, min_value(result(board, move)))
            if v == 1:
                return v
    return v
def min_value(state):
    if terminal(state):
        return utility(state)
    else:
        v = +inf
        for move in empty_cells(state):
            v = min(v, max_value(result(state, move)))
            if v == -1:
                return v
    return v
winner = None
print_field()

while not terminal(board):
    user_coord = int(input(«Enter the coordinates:»))
    if user_coord in empty_cells(board):
        update_field(user_coord)
        print_field()
        if win(board):
            print(f"{player(board)} won»)
            break
    comp_coord = minimax(board)
    update_field(comp_coord)
    print_field()
    if win(board) is not None:
        print(f"{winner} won»)

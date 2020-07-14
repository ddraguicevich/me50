"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is X:
                x_count += 1
            elif board[i][j] is O:
                o_count += 1
    if (x_count <= o_count):
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                available_moves.add((i,j))
    return available_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    local_board = copy.deepcopy(board)
    moves = actions(local_board)
    (i, j) = action
    if action not in moves:
        raise IndexError('Invalid Move')
    else:
        which_player = player(local_board)
        local_board[i][j] = which_player
    return local_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] != EMPTY):
            return board[i][0]
        elif (board[0][i] == board[1][i] == board[2][i] != EMPTY):
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2] != EMPTY):
            return board[0][0]
    elif (board[0][2] == board[1][1] == board[2][0] != EMPTY):
            return board[0][2]
    else:
        return EMPTY


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    moves = actions(board)
    if not moves:
        return True
    elif winner(board) is not EMPTY:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result is X:
        return 1
    elif result is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def score(board):
        """
        Returns score for a particular board
        """
        current_score = int()
        if terminal(board):
            return utility(board)
        else:
            if player(board) is X:
                current_score = -2
                for move in actions(board):
                    current_score = max(current_score, score(result(board, move)))
            else:
                current_score = 2
                for move in actions(board):
                    current_score = min(current_score, score(result(board, move)))
            return current_score
    best_move = tuple()
    best_score = int()
    if terminal(board):
        return EMPTY
    else:
        if player(board) is X:
            best_score = -2
            for move in actions(board):
                if score(result(board, move)) > best_score:
                    best_score = score(result(board, move))
                    best_move = move
        else:
            best_score = 2
            for move in actions(board):
                if score(result(board, move)) < best_score:
                    best_score = score(result(board, move))
                    best_move = move
    return best_move
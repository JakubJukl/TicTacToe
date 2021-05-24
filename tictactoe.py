"""
Tic Tac Toe Player
"""

import math
import pdb 
import copy

X = "X"
O = "O"
EMPTY = None
NUMBER_OF_ROWS = 3

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
    count = [0, 0]  #count = (count_x, count_o)
    possible_actions = set()
    for i in range(NUMBER_OF_ROWS):
        for j in range(NUMBER_OF_ROWS):
            character = board[i][j]
            if character == X:
                count[0]+=1
                if count[0]  == 5:
                    return X
            elif character == O:
                count[1]+=1
                if count[1] == 5:
                    return O
    if count[0] < count[1]:
        return X
    else: 
        return O
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(NUMBER_OF_ROWS):
        for j in range(NUMBER_OF_ROWS):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions
                
        


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not board[action[0]][action[1]] == EMPTY:
        raise Exception("This action can't be taken")
    copiedboard = copy.deepcopy(board)
    copiedboard[action[0]][action[1]] = player(board)
    return copiedboard  


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return term_and_winner(board)[1]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return term_and_winner(board)[0]


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == initial_state():
        return (0,1)
    return recursion(board)[1]

def recursion(board):
    """
    Returns tuple of evaluation of the final state of the action and optimal action
    """
    v = -2
    if terminal(board):
        optimal = None
        return utility(board), optimal
    else:
        possible_actions = actions(board)
        for action in possible_actions:
            futureBoard = result(board, action)
            recursive_tuple = recursion(futureBoard)
            if player(board) == X:
                if recursive_tuple[0] == 1:
                    optimal = action
                    v = 1
                    break
                if recursive_tuple[0] > v:
                    optimal = action
                    v = recursive_tuple[0]
            else:
                if recursive_tuple[0] == -1:
                    optimal = action
                    v = -1
                    break
                if recursive_tuple[0] < abs(v):    
                    optimal = action
                    v = recursive_tuple[0]
    return v, optimal
            
        
            

def term_and_winner(board):
    """
    Returns tuple with boolean, if the game is over and the winner.
    """
    for i in range(-2,1, 2):
        if not (board[1][1] == EMPTY) and (board[0][i + 2] == board[1][1] and board[1][1] == board[2][i * -1]):
            return True, board[1][1]
    for i in range(NUMBER_OF_ROWS):
        if not (board[i][1] == EMPTY) and (board[i][0] == board[i][1] and board[i][1] == board[i][2]):
           return True, board[i][1]
        if not (board[1][i] == EMPTY) and (board[0][i] == board[1][i] and board[1][i] == board[2][i]):
           return True, board[1][i]
    for i in range(NUMBER_OF_ROWS):
        if EMPTY in board[i]:         
            return False, 'Error'
    return True, None



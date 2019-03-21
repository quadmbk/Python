#!/bin/env python


BOARD = [];
SIZE = 0
def init(size):
    SIZE = size
    for i in range(SIZE):
        BOARD.append([0] * SIZE);
    display() 

def display(size=SIZE):
    print "  ",
    for index in range(size):
        print index,"",
    print
    for count,row in enumerate(BOARD):
        print count,row

def horizontal(board_arg=BOARD):
    msg = "Horizontally"
    for row in board_arg:
            if row.count(row[0]) == len(row) and row[0] != 0:
                print "Player ",row[0]," WINS ",msg," !!"
                return True
    return False

def vertical(board_arg=BOARD):
    msg = "Vertically"
    transpose = [];
    for col_index in range(len(board_arg[0])):
        check = [];
        for row in board_arg:
            check.append(row[col_index])
        transpose.append(check)

    for col in transpose:
        if col.count(col[0]) == len(col) and col[0] != 0:
            print "Player ",col[0]," WINS ", msg," !!"
            return True

    return False



def diagonal(board_arg=BOARD):
    msg = "Diagonally "
    length = len(board_arg[0])
    front_diagonal = []
    reverse_diagonal = []
    for item in range(length):
        front_diagonal.append(board_arg[item][item])
    for item in range(length):
        reverse_diagonal.append(board_arg[item][length-1])
        length -= 1
    if (front_diagonal.count(front_diagonal[0]) == len(front_diagonal) and front_diagonal[0] != 0):
        print "Player ",front_diagonal[0]," WINS ",msg,"!!"
        return True
    elif (reverse_diagonal.count(reverse_diagonal[0]) == len(reverse_diagonal) and reverse_diagonal[0] != 0):
        print "Player ",reverse_diagonal[0]," WINS ",msg,"!!"
        return True
    else:
        return False

def win():
    status = False
    status = horizontal()
    if status == True:
        return True
    status = vertical()
    if status == True:
        return status
    status = diagonal()
    if status == True:
        return status

def game_board(board_arg=BOARD,player=1,row=0,col=0,size=SIZE):
    try:
        board_arg[row][col] = player
        display(size)
        #for count,row in enumerate(board_arg):
        #    print count,row

    except IndexError as e:
        print "Index can't be more than 2.",e;
    except Exception as e:
        print "Unexcepted Exception. ", e;

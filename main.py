#!/bin/env python
import os
from GameModule import *

size = int(input ("Enter Size:"));
init(size);
play = True
status = False
while play == True:
    for player in [1,2]:
        os.system('clear')
        display(size)
        print 
        print
        print "Current Player : ",player
        row_selected = int(input("Enter Row : "))
        column_selected = int(input("Enter Column: "))
        game_board(BOARD,player,row_selected,column_selected,size)
        status = win()
        if status == True:
            play = False
            break

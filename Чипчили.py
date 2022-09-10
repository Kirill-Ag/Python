import random

def displayBoard(board):
    # Эта функция выволит на экран игровое поле,
    # клетки которого будут заполнятся

    # "board" - это список в котором хранится 10 сторк
    # для прорисовки игрового поля (индекс 0 ингрорируется)

    print(boarprd[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-') 
    print(board[4]+'|'+board[5]+'|'+board[6]) 
    print('-+-+-') 
    print(board[1]+'|'+board[2]+'|'+board[3])
def inputPlayerLetter(): 
    letter = ''
    while not (letter=='X' or letter=='O'):
        print('''   Виберите "X" или "O".
        На английской раскладке.''')


    #ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
    displayBoard(['A','O',' ',' ','X',' ',' ','X',' ','O'])
    
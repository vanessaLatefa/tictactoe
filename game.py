from random import randint
import os

os.system("clear")

class Board :

    def __init__(self):
        self.squares = [" "] * 9


    def printBoard(self):
        print('')
        print (self.squares[0], ' |', self.squares[1], ' |', self.squares[2])
        print('------------')
        print (self.squares[3], ' |', self.squares[4], ' |', self.squares[5])
        print('------------')
        print (self.squares[6], ' |', self.squares[7], ' |', self.squares[8])


    def updateBoard(self,square_number, player):
        print('updating board..')
        if self.squares[square_number] == ' ':
            print(player)
            self.squares[square_number] = player

class Game():

    def welcome(self):
        print('Welcome to TIC TAC TOE')

    def refresh(self):
        os.system("clear")
        self.welcome()
        b = Board()
        b.printBoard()      

def main():

    b = Board()
    g = Game()

    while True :
        g.refresh()
        player = int(input('\n[X] Choose between 0-8 >>> '))
        b.updateBoard(player, 'X')
        
        
if __name__ == "__main__":
    main()
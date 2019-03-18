from random import randint



class Board :
    #initializing the board using a list
    def __init__(self):
        self.squares = [' '] * 10

    #printing the squares of board by list index
    def printBoard(self):
        print('')
        print (self.squares[1], ' |', self.squares[2], ' |', self.squares[3])
        print('------------')
        print (self.squares[4], ' |', self.squares[5], ' |', self.squares[6])
        print('------------')
        print (self.squares[7], ' |', self.squares[8], ' |', self.squares[9])


    def updateBoard(self,square_number, move):
        if self.squares[square_number] == ' ':  
            self.squares[square_number] = move
    
    def checkForMove(self, char,s1,s2,s3):
        if self.squares[s1] == char and self.squares[s2] == char and self.squares[s3] == char:
            return True

    def checkWins(self,char):
        if self.checkForMove(char, 1,2,3):
            return True
        if self.checkForMove(char, 4,5,6):
            return True
        if self.checkForMove(char, 7,8,9):
            return True
        if self.checkForMove(char, 1,4,6):
            return True
        if self.checkForMove(char, 3,6,9):
            return True
        if self.checkForMove(char, 1,5,7):
            return True
        if self.checkForMove(char, 3,5,9):
            return True    

        for i in self.squares:
            if i == i :
                return False
            else:
                print('Try again')
                self.printBoard()

        


class Game:

    def welcome(self):
        print('Welcome to TIC TAC TOE')#header

    def refresh(self): #self refers to Game class
        os.system('clear')
        self.welcome()
        b = Board()#instance of the Board Class
        b.printBoard()      

def main():

    b = Board()
    g = Game()

    g.refresh()
    while True:
        
        your_move = int(input('\n[X] Choose between 1-9 >>> '))
        b.updateBoard(your_move, 'X')
        b.printBoard()
        
        print('[O] COMPUTER\'S TURN')
        computer_move = randint(1,10)
        b.updateBoard(computer_move, 'O')
        b.printBoard()
        
        if b.checkWins('O') == True:
            print('COMPUTER WINS!')
            break
        elif b.checkWins('X')== True:
            print('YOU WIN!')
            break
        
        
        
if __name__ == "__main__":
    main()
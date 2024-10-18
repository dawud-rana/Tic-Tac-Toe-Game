import math, time
from player import RealPlayer, EasyComputerPlayer, HardComputerPlayer

class game():
    def __init__(self) -> None:
        self.board = self.create_board()
        self.current_winner = None
    
    #Creating the gameboard intially
    @staticmethod
    def create_board():
        return [' ' for _ in range(9)]
    
    #Prints the gameboard in its current state
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        
    
    #Prints the space numbers in the beginning of the game for players' reference
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    
    #Executes the current player's move and checks to see if they won with their move
    def move(self, space, letter):
        if self.board[space] == ' ':
            self.board[space] = letter
            if self.win(space, letter):
                self.current_winner = letter
            return True
        return False
    
    #Checks a player to see if they won after playing their last move
    def win(self, space, letter):

        #Find row number then retrieve row to check if all letters are the same
        row_index = math.floor(space/3)
        row = self.board[row_index*3:(row_index+1)*3]
        if all(s == letter for s in row):
            return True

        #Find column number then retrieve column to check if all letters are the same
        col_index = space%3
        col = [self.board[col_index+i*3] for i in range(3)]
        if all (s == letter for s in col):
            return True
        

        if space%2 == 0:

            #Checks first possible diagonal
            d1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in d1]):
                return True
            
            #Check second possible diagonal
            d2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in d2]):
                return True
            
        #No winner is found if no row, column, or diagonal has the desired letter in every space  
        return False 
    
    #Determines whether any spaces on the gameboard are empty
    def empty_spaces(self):
        return ' ' in self.board
    
    #Provides quantity of how many empty spaces are currently on the gameboard
    def empty_spaces_count(self):
        return self.board.count(' ')
    
    #Keeps track of all the current positions which can be played
    def available_spaces(self):
        return [i for (i, x) in enumerate(self.board) if x == ' ']
    
def play(game, player1, player2, print_game=True):
    if print_game:
        game.print_board_nums()
        print(' ')
    
    letter = 'X'
    while game.empty_spaces():
        if letter == 'O':
            space = player2.get_move(game)
        else:
            space = player1.get_move(game)
        if game.move(space, letter):
            
            if print_game:
                print(letter + ' has chosen to take space #{}'.format(space))
                game.print_board()
                print('')
            
            if game.current_winner:
                if print_game:
                    print(letter + ' has won the game!')
                return letter
            letter = 'O' if letter == 'X' else 'X'

        time.sleep(.8)

    if print_game:
            print('Both players have tied!')

if __name__ == '__main__':
    print('Welcome to Tic-Tac-Toe!\nPick your game version')
    valid_entry = False
    while not valid_entry:
        version = input('Two-Player (1),  Easy Computer Opponent (2),  Hard Computer Opponent (3): ')
        try:
            v = int(version)
            if v not in range(1, 4):
                raise ValueError
            valid_entry = True
        except ValueError:
            print("Invalid Selection. Please try again.")

    player1 = RealPlayer('X')
    if v == 1:
        player2 = RealPlayer('O')
    elif v == 2:
        player2 = EasyComputerPlayer('O')
    elif v == 3:
        player2 = HardComputerPlayer('O')
    tictactoe = game()
    play(tictactoe, player1, player2, print_game=True)

           

    

    


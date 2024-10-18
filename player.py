import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, tictactoe):
        pass

class RealPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, tictactoe):
        valid_space = False
        s = None                            #The ineteger representing the space the player is attempting to move to
        while not valid_space:
            space = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                s = int(space)
                if s not in tictactoe.available_spaces():
                    raise ValueError
                valid_space = True
            except ValueError:
                print('Invalid space. Try again.')
        return s
    
class EasyComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, tictactoe):
        s = random.choice(tictactoe.available_spaces())
        return s
    
class HardComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, tictactoe):
        if tictactoe.empty_spaces == 9:
            s = random.choice(tictactoe.available_spaces())
        else:
            s = self.minimax(tictactoe, self.letter)['space']
        return s
    
    def minimax(self, state, player):
        max_p = self.letter
        opponent_p = 'X' if player == 'O' else 'O'

        #Check if a player has one or if there has been a draw
        if state.current_winner == opponent_p:
            return {'space': None, 'score': 1*(state.empty_spaces_count()+1) if opponent_p == max_p else -1*(state.empty_spaces_count()+1)}
        elif not state.empty_spaces():
            return {'space': None, 'score': 0}
        
        #Default score to later maximize or minimize depending on the current 'player'
        if player == max_p:
            best_score = {'space': None, 'score': -math.inf}
        else:
            best_score = {'space': None, 'score': math.inf}

        for options in state.available_spaces():
            #Make a possible move
            state.move(options, player)
            #Simulate more possible games after this move was made
            sim_score = self.minimax(state, opponent_p)
            #Undo the move after
            state.board[options] = ' '

            state.current_winner = None
            sim_score['space'] = options

            #Maximizes or Minimizes depending on the current 'player'
            if player == max_p:
                if sim_score['score'] > best_score['score']:
                    best_score = sim_score
            
            else:
                if sim_score['score'] < best_score['score']:
                    best_score = sim_score
            
        return best_score




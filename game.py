# this program runs with tic-tac-toe 
# 49:05

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3x3 board
        self.current_winner = None # keep track on winner
        
    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i*3:(i+1)*3]] for i in range(3):
            print('| ' + ' | '.join(row) + ' |')
            
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tell us what number correponds to what box)
        number_board = [[str(1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        
    def empty_squares(self):
        return ' ' in self.board
        
    def num_empty_squares(self):
        return self.board.count(' ')
        
    def make_move(self, square, letter):
        # if valid move, then make the move (assign square to letter)
        # then return true. If vlid, return false
        if sel.board[square] == ' ':
            self.board[square] = letter
            return True
        return False
        
        
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
        
    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # (we do not have to worry about the winner because we'll just return that
    # which breaks the loop)
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
            
        
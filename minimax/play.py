from tictactoe import Game
from player import Player

g = Game()
g.board[0][0] = 1
g.board[1][0] = 1
g.board[2][0] = 1
g.board[0][1] = -1
g.board[0][2] = -1
g.winner()
g.display_board()

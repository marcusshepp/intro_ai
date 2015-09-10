from tictactoe import Game
from player import Player

g = Game()
g.board[0][0] = 1
g.board[1][0] = 1
g.board[2][0] = -1
g.board[0][1] = -1
g.board[1][1] = -1
g.board[2][1] = 1
g.board[0][2] = 1
g.board[1][2] = 1
g.board[2][2] = -1
if g.draw():
    print "Draw"
    print g.display_board()
else:
    print g.winner()
    print g.display_board()

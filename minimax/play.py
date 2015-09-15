from minimax.tictactoe import Game
from minimax.cpu_player import CPUPlayer

g = Game()
cpu = CPUPlayer(piece=-1)
while not g.is_there_a_winner():
    x = raw_input()
    x = int(x)
    y = raw_input()
    y = int(y)
    piece = raw_input()
    piece = int(piece)
    g.move(x, y, piece)
    g.move(*cpu.random_move())

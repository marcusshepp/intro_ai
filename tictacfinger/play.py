import random as rand

from tictacfinger.tictactoe import Game
from tictacfinger.cpu_player import CPUPlayer


if __name__ == "__main__":
    start_text = """
    Tic Tac Toe
    Human vs CPU

    How to play:
    Enter: 0, 1 or 2
    First value is the row.
    Second value is the column.
    You are "X".
    The CPU is "O".
    
    Example:
    [in]:
    1
    1
    [out]:
    [" ", " ", " "]
    [" ", "X", " "]
    [" ", " ", " "]
    """
    print start_text
    g = Game()
    init_cpu = {"piece":-1, "game":g}
    cpu = CPUPlayer(**init_cpu)
    rand_num = rand.randint(0, 1)
    if rand_num == 1:
        print "Human goes first"
        while not g.there_is_a_winner():
            # u = user
            u_x = raw_input()
            u_x = int(u_x)
            u_y = raw_input()
            u_y = int(u_y)
            g.move(u_x, u_y, 1)
            g.display_board()
            if g.draw(): 
                break
            if g.there_is_a_winner():
                break
            g.move(**cpu.level_three())
            g.display_board()
        g.display_winner()
    else:
        print "CPU goes first"
        while not g.there_is_a_winner():
            g.move(**cpu.level_three())
            g.display_board()
            if g.draw(): 
                break
            if g.there_is_a_winner():
                break
            # u = user
            u_x = raw_input()
            u_x = int(u_x)
            u_y = raw_input()
            u_y = int(u_y)
            g.move(u_x, u_y, 1)
            g.display_board()
        g.display_winner()
        
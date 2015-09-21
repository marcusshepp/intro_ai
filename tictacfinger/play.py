from tictacfinger.tictactoe import Game
from tictacfinger.cpu_player import CPUPlayer


if __name__ == "__main__":

    g = Game()
    init_cpu = {"piece":-1, "game":g}
    cpu = CPUPlayer(**init_cpu)
    while not g.there_is_a_winner():
        # u = user
        u_x = raw_input()
        u_x = int(u_x)
        u_y = raw_input()
        u_y = int(u_y)
        g.move(u_x, u_y, 1)
        g.display_board()
        g.move(**cpu.level_two())
        g.display_board()
    g.display_winner()

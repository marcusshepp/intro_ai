class Game(object):

    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]

    def move(self, x, y, piece):
        """
        replaces the x and y coordinates of the board
        with +1 or -1.
        +1 == x
        -1 == o
        """
        self.board[x][y] = piece
        return self.display_board()

    def display_board(self):
        print self.board[0]
        print self.board[1]
        print self.board[2]
        return

class Game(object):

    def __init__(self):
        self.board = [[0 for x in range(3)] for i in xrange(3)]

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

    def board_contains_empty_spaces(self):
        for row in self.board:
            if all(v == 0 for v in row):
                continue
            else:
                return False
        return True

    def winner(self):
        board = self.board
        row_zero = [v for v in board[0]]
        row_one = [v for v in board[1]]
        row_two = [v for v in board[2]]
        column_zero = [row[0] for row in board]
        column_one = [row[1] for row in board]
        column_two =[row[2] for row in board]
        forward_slash = []
        forward_slash.extend(
            [board[0][2],
            board[1][1],
            board[2][0]])
        backward_slash = []
        backward_slash.extend(
            [board[0][0],
            board[1][1],
            board[2][2]])
        x = [
            row_zero,
            row_one,
            row_two,
            column_zero,
            column_one,
            column_two,
            forward_slash,
            backward_slash]
        x = [sum(i) for i in x]
        p = ""
        for s in x:
            if s == -3:
                p += "O wins!"
            elif s == 3:
                p += "X wins!"
            else:
                continue
        print p

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
        zero = self.board[0]
        one = self.board[1]
        two = self.board[2]
        return "{0}\n{1}\n{2}".format(zero, one, two)

    def board_contains_empty_spaces(self):
        for row in self.board:
            if all(v == 0 for v in row):
                continue
            else:
                return False
        return True

    def possible_win_combinations(self):
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
        all_possible_win_combinations = [
            row_zero,
            row_one,
            row_two,
            column_zero,
            column_one,
            column_two,
            forward_slash,
            backward_slash]
        return all_possible_win_combinations

    def draw(self):
        if not self.board_contains_empty_spaces():
            if self.winner() == "":
                return True
        return False

    def winner(self):
        sums_of_win_combinations = [
            sum(i) for i in self.possible_win_combinations()]
        return_value = ""
        for sum_ in sums_of_win_combinations:
            if sum_ == -3:
                return_value += "O wins!"
            elif sum_ == 3:
                return_value += "X wins!"
            else:
                continue
        return return_value

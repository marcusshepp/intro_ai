import itertools
import copy

class Game(object):

    """
    A game of Tic Tac Toe.
    Contains methods that will be useful to a computer
    learning to evaluate board moves.
    """

    def __init__(self):
        self.board = [
            [0 for x in range(3)] for i in xrange(3)]

    def move(self, x, y, piece):
        """
        replaces the x and y coordinates of the board
        with +1 or -1.
        +1 == X
        -1 == O
        """
        if not self.draw():
            if x < 3 and y < 3:
                if self.board[x][y] == 0:
                    self.board[x][y] = piece
                    return
                else: return self.error_messages("occupied")
            else: return self.error_messages("Invalid Input")
        else: print "Draw."

    def draw(self):
        """
        Checks if there is a draw on the board.
        """
        if len(self.empties()) == 0:
            print "no empties"
            return True
        else: return False
    
    def error_messages(self, type_of_message):
        if type_of_message == "occupied":
            print "That space on the board is occupied!"
            print "Please try again."
            u_x = raw_input()
            u_x = int(u_x)
            u_y = raw_input()
            u_y = int(u_y)
            self.move(u_x, u_y, 1)
            self.display_board()
        if type_of_message == "Invalid Input":
            print "Enter x, y coordinates!"
            print "Please only use values 0-2."

    def display_board(self):
        """
        Displays the current state of the board.
        """
        board = copy.deepcopy(self.board)
        for x in xrange(3):
            for y in xrange(3):
                if board[x][y] == -1:
                    board[x][y] = "O"
                elif board[x][y] == 1:
                    board[x][y] = "X"
                else: board[x][y] = " "
        print board[0]
        print board[1]
        print board[2]
        print "\n"
        return

    def display_winner(self):
        """ If there's a winner display who won. """
        for combo in self.possible_win_combinations():
            if sum(combo) == -3:
                print "Player: \"O\", wins"
                return
            elif sum(combo) == 3:
                print "Player: \"X\", wins"
                return
        print "no winner"
        return

    def possible_win_combinations(self):
        """
        Enumerates and :returns: all eight
        possible win cominations for the current board.
        [[], [], [], ...]
        """
        board = self.board
        row_zero = [v for v in board[0]]
        row_one = [v for v in board[1]]
        row_two = [v for v in board[2]]
        column_zero = [row[0] for row in board]
        column_one = [row[1] for row in board]
        column_two =[row[2] for row in board]
        forward_slash = [
            board[0][2],
            board[1][1],
            board[2][0]]
        backward_slash = [
            board[0][0],
            board[1][1],
            board[2][2]]
        return [
            row_zero, row_one, row_two,
            column_zero, column_one, column_two,
            forward_slash, backward_slash]

    def there_is_a_winner(self):
        """
        Checks the current board for a winner.
        :returns:
        True if there is a winner.
        else: False
        """
        pwc = self.possible_win_combinations()
        pwc = [sum(combo) for combo in pwc]
        def combo_wins(combo_sum):
            # boolean winner indicator
            if combo_sum == 3 or combo_sum == -3:
                return True
            else: return False
        list_of_boolean_indicators = [
            combo_wins(combo) for combo in pwc]
        # if any combination is a winner
        if any(list_of_boolean_indicators):
            return True
        else: return False

    def empties(self):
        """
        return a list of tuples.
        each tuple is an available board
        position.
        """
        tuples = []
        def zero(n):
            if n == 0: return True
            return False
        for x in xrange(3):
            for y in xrange(3):
                if zero(self.board[x][y]):
                    tuples.append((x, y))
        return tuples

    def this_creates_a_win(self, x, y, piece):
        """
        Return True
        If move creates win
        Else False
        """
        move = {"x": x, "y": y, "piece": piece}
        self.move(**move)
        if self.there_is_a_winner():
            self.board[x][y] = 0
            return True
        self.board[x][y] = 0
        return False

    def move_creates_n_possible_wins(self, x, y, piece):
        """
        returns the number of possible win
        combinations a move can yield.
        """
        self.board[x][y] = piece
        i = 0
        for e in self.empties():
            if self.this_creates_a_win(e[0], e[1], piece):
                i += 1
        self.board[x][y] = 0
        return i

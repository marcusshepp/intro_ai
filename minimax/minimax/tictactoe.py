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
        if x < 3 and y < 3:
            if self.board_contains_empty_spaces():
                if self.board[x][y] == 0:
                    self.board[x][y] = piece
                    return self.display_board()
                else: return self.error_messages("occupied")
        else: return False

    def error_messages(self, type_of_message):
        if type_of_message == "occupied":
            print "That space on the board is occupied!"
            print "Please try again."

    def display_board(self):
        """
        Displays the current state of the board.
        """
        print self.board[0]
        print self.board[1]
        print self.board[2]
        print "\n"
        return

    def board_contains_empty_spaces(self):
        """ 
        Does the current board contain empty spaces? 
        """
        for row in self.board:
            if any(v == 0 for v in row):
                continue
            else:
                return False
        return True

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

    def is_there_a_winner(self):
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
        
    def display_winner(self):
        """ If there's a winner display who won. """
        if self.is_there_a_winner():
            # find who won
            for combo in self.possible_win_combinations():
                if sum(combo) == -3: return "Player: \"O\", wins"
                elif sum(combo) == 3: return "Player: \"X\", wins"
        else: return "no winner"
        
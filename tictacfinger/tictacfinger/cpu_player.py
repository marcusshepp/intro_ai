import random as rand


class CPUPlayer(object):
    """
    notes:
    - list of empties only move on those
    - temp value at a zero if not a win put back to zero
    - one instance of board
    """
    def __init__(self, piece, game):
        self.piece = piece
        """
        Take the game instance in on
        init to have access to all attr
        and methods.
        """
        self.game = game

    def level_zero(self):
        """
        CPU puts its piece in a random
        available spot on board.
        """
        empties = self.game.empties()
        i = rand.randint(0, len(empties))
        piece = self.piece
        coor = empties[i]
        move = {"x": coor[0], "y": coor[1], "piece": piece}
        return move

    def level_one(self):
        """
        CPU puts its piece in an
        available space that creates a
        win if available,
        else randomly selects a spot.
        """
        empties = self.game.empties()
        for e in empties:
            if self.game.this_creates_a_win(e[0], e[1], self.piece):
                move = {"x": e[0], "y": e[1], "piece": self.piece}
                return move
        return self.level_zero()

    def level_two(self):
        """
        Will win if possible. 
        Else CPU will block Humans from winning.
        """
        empties = self.game.empties()
        for e in empties:
            # if CPU can win make that move
            if self.game.this_creates_a_win(e[0], e[1], self.piece):
                move = {"x": e[0], "y": e[1], "piece": self.piece}
                return move
        for e in empties:
            # if Human can win block that move
            if self.game.this_creates_a_win(e[0], e[1], 1):
                move = {"x": e[0], "y": e[1], "piece": self.piece}
                return move
        # if no one can win make random move
        return self.level_zero()
    
    def level_three(self):
        """
        CPU will put a piece in a place that
        will create a win for itself
        on next turn.
        """
        pass
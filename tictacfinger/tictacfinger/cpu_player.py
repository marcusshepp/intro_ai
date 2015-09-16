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

    def level_one(self):
        """
        CPU puts its piece in a random
        available spot on board.
        """
        empties = self.game.empties()
        i = rand.randint(0, len(empties))
        piece = self.piece
        coor = empties[i]
        move = {
        "x": coor[0],
        "y": coor[1],
        "piece": piece
        }
        return move

    def level_two(self):
        """
        CPU puts its piece in an
        available space that creates a
        win if available,
        else randomly selects a spot.
        """
        pass

    def level_three(self):
        """
        """
        pass

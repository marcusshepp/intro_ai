import random as ran


class CPUPlayer(object):
    
    def __init__(self, piece):
        self.piece = piece

    def random_move(self):
        x = ran.randint(0, 2)
        y = ran.randint(0, 2)
        piece = self.piece
        return [x, y, piece]

import copy

from cpu_player import CPUPlayer

class Minimax(CPUPlayer):
    
    board_copy = copy.deepcopy(self.game.board)
    
    def move(self):
        moves = self.empties(self.board_copy())
        best_move = moves[0]
        best_score = float("-inf")
        for move in moves:
            # check the moves score
        
    def maximize(self):
        pass
        
    def minimize(self):
        pass
        
    def empties(self, board):
        empties = []
        for x in xrange(3):
            for y in xrange(3):
                if board[x][y] == 0:
                    empties.append((x, y))
        return empties
    
    def score_a_move(self, x, y, piece):
        self.board_copy[x][y] = piece
        possible_wins = 0
        for e in self.empties(self.board):
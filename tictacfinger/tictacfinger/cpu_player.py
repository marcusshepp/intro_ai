import random as rand
import operator

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
        print "Making a random move"
        empties = self.game.empties()
        i = rand.randint(0, len(empties)-1)
        piece = self.piece
        coor = empties[i]
        move = {"x": coor[0], "y": coor[1], "piece": piece}
        return move

    def level_three(self):
        """
        CPU will put a piece in a place that
        will create a win for itself
        on next turn.
        """
        empties = self.game.empties()
        for e in empties:
            # if CPU can win make that move
            if self.game.this_creates_a_win(e[0], e[1], self.piece):
                move = {"x": e[0], "y": e[1], "piece": self.piece}
                print "Winning takes priority"
                return move
        num_of_possible_human_wins = 0
        m = ()
        for e in empties:
            # if Human can win block that move
            if self.game.this_creates_a_win(e[0], e[1], 1):
                num_of_possible_human_wins += 1
                m = (e[0], e[1])
        if num_of_possible_human_wins > 1:
            print "GG"
            move = {"x": m[0], "y": m[1], "piece": self.piece}
            print "Blocking Opponent"
            return move
        elif num_of_possible_human_wins == 1:
            print "gotcha!"
            move = {"x": m[0], "y": m[1], "piece": self.piece}
            return move
        # predicting a move that will yield the most
        # possible win combos on next move.
        print "looking two moves deep"
        best_win_combos = {}
        for e in self.game.empties():
            num_of_possible_wins = self.game.move_creates_n_possible_wins(
                e[0], e[1], self.piece)
            if num_of_possible_wins > 0:
                best_win_combos[(e[0], e[1])] = num_of_possible_wins
        if len(best_win_combos.values()) > 0:
            # print best_win_combos
            max_prediction = max(
                best_win_combos.iteritems(), key=operator.itemgetter(1))[0]
            # print max_prediction
            sp = max_prediction
            move = {"x": sp[0], "y": sp[1], "piece": self.piece}
            return move
        return self.look_deeper()

    def look_deeper(self):
        print "looking deeper"
        best_win_combos = {}
        for first_move in self.game.empties():
            self.game.move(first_move[0], first_move[1], self.piece)
            for second_move in self.game.empties():
                best_win_combos[(first_move, second_move)] = self.game.move_creates_n_possible_wins(
                    second_move[0], second_move[1], self.piece)
            self.game.undo_move(first_move[0], first_move[1], self.piece)
        if best_win_combos:
            x = max(best_win_combos.iteritems(), key=best_win_combos.get)[0][0][0]
            y = max(best_win_combos.iteritems(), key=best_win_combos.get)[0][0][1]
            move = {"x": x, "y": y, "piece": self.piece}
            return move
        else: return self.level_zero()

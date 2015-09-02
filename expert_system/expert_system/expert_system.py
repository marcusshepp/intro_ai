"""
Guess your teir.
Assignment one of Intro to AI.
"""
from data.questions import questions
from data.possible_teirs import possible_teirs


class User(object):
    """
        A user object that will:
        Hold the current state of the `teir` sting.
    """
    current_score = 0

    def _is(self):
        for i in xrange(12): self.current_score += questions.get(i)
        for teir in possible_teirs:
            if self.current_score in possible_teirs[teir]:
                return teir

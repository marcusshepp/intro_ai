"""
Guess your teir.
Assignment one of Intro to AI.
"""
from data.questions import questions
from data.possible_tiers import possible_tiers


class User(object):
    """
        A user object that will:
        Hold the current state of the `teir` sting.
    """

    def __init__(self):
        self.current_score = 0

    def _is(self):
        for i in xrange(12): self.current_score += questions.get(i)
        for tier in possible_tiers:
            if self.current_score in possible_tiers[tier]:
                return tier

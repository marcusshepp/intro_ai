from django.db import models

class Game(models.Model):

    class Meta:
        ordering = ["-id"]

    PLAYERS = [
        ("cpu", "CPU"),
        ("human", "Human"),
        ("draw", "Draw"),
    ]
    STATES = [
        ("cpu", "CPU"),
        ("human", "Human"),
        ("draw", "Draw"),
    ]
    outcome = models.CharField(max_length=10, choices=PLAYERS)
    state = models.CharField(max_length=10, choices=STATES)

class Board(models.Model):

    class Meta:
        ordering = ["-id"]
    game = models.ForeignKey(Game)
    one = models.IntegerField()
    two = models.IntegerField()
    three = models.IntegerField()
    four = models.IntegerField()
    five = models.IntegerField()
    six = models.IntegerField()
    seven = models.IntegerField()
    eight = models.IntegerField()
    nine = models.IntegerField()

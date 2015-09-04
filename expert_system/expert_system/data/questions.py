"""
Plays a blame game with the User.
They must give self criticism to do well.
"""
from utilities import print_display, append_possible_answers


def introduction():
    display = "\nYou'll be asked a series of ten questions.\nPlease answer these question with:\n"
    print append_possible_answers(display)
    display = "At the end of this survey,\nI will accurately perdict what LOL tier you are.\n"
    print display
    return 0

def q0():
    display = "\nYou're mid.\nYou die under tower 2 vs. 1.\nMeanwhile, your jungler is farming wolves:"
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q1():
    display = "\nYou're top with teleport off cooldown.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q2():
    display = "\nYou're the jungler.\n2.25 min into the game.\nEnemy Mid Invades.\nYou lose blue and die.\n"
    display += "Ally Mid doesn't MIA or follow."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q3():
    display = "\n50 min into the game.\nAll 6 inhibs down.\nYour team agrues whether to do Baron or push.\n"
    display += "Enemy backdoors."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q4():
    display = "\nYou're ADC.\n8 min into the game.\nYou farmed up BF and go to base.\nSupport dies 2 v 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q5():
    display = "\n25 min into the game.\nDrag and Baron live.\nYou want to baron.\n"
    display += "Your team starts Drag.\nEnemy gets Baron."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q6():
    display = "\nYou're Supporting.\nYou ward for your Mid.\nEnemy Jungler clears the ward.\nMid dies 2 v 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q7():
    display = "\nYou're playing Bard.\nYou ult your own teammate.\nThey die 1 v 5."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q8():
    display = "\nYou're mid as Zed.\nYour KDA is 20-0-1.\nYour team loses the game."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q9():
    display = "\nYou're playing a tank with CC.\n35 min into the game.\nYou Initiate.\nYour ADC dies from Enemy tank."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q10():
    display = "\nYou're Annie.\nLand a five man stun with Tibbers.\nTeam just out of range to follow up in time.\nYou die 1 v 5."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

questions = {
    0: introduction(),
    1: q0(),
    2: q1(),
    3: q2(),
    4: q3(),
    5: q4(),
    6: q5(),
    7: q6(),
    8: q7(),
    9: q8(),
    10: q9(),
    11: q10(),
}

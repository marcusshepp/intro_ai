"""
plays a blame game.
"""

def print_display(a, display):
    if type(a) is int:
        print display
    else:
        return

def append_possible_answers(display):
    possible_answers = "Your Fault: 0, Their Fault: 1"
    string = "{d}\n{pa}".format(d=display, pa=possible_answers)
    return string

def q0():
    display = "You're mid and die under tower 2 vs. 1.\n\
Meanwhile: your jungler is farming wolves:"
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q1():
    display = "You're top.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q2():
    display = "You're the jungler.\n2.25 min into the game.\nEnemy Mid Invades.\nYou lose blue and die."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q3():
    display = "You're top.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q4():
    display = "You're top.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q5():
    display = "You're top.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q6():
    display = "You're top.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q7():
    display = "You're mid and die under tower 2 vs. 1.\n\
Meanwhile: your jungler is farming wolves:"
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q8():
    display = "You're top.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q9():
    display = "You're top.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q10():
    display = "You're top.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q11():
    display = "You're top.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

def q12():
    display = "You're top.\n20 min into the game.\nTeam Initiates.\nThey all die 4 for 1."
    print append_possible_answers(display)
    val = raw_input()
    return int(val)

questions = {
    0: q0(),
    1: q1(),
    2: q2(),
    3: q3(),
    4: q4(),
    5: q5(),
    6: q6(),
    7: q7(),
    8: q8(),
    9: q9(),
    10: q10(),
    11: q11(),
    12: q12(),
}

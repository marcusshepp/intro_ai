def print_display(a, display):
    if type(a) is int:
        print display
    else:
        return

def append_possible_answers(display):
    possible_answers = "Your Fault: 1, Their Fault: 0"
    string = "{d}\n{pa}\n".format(d=display, pa=possible_answers)
    return string

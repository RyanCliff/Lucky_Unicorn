# Make Function
def yes_no(question):
    valid = False
    while not valid:
        answer = input(question).lower()
        if answer == "yes" or answer == "y":
            print("start game")
            return answer
        elif answer == "no" or answer == "n":
            print("display instructions")
            return answer
        else:
            print("Please pick yes or no.")

def instructions():
    print("***How To Play***")
    print()
    print("The rules of the game are.")
    print()
    return ""


# Main Routine
show_instructions = yes_no("Have you played the Lucky Unicorn game before? ")
if show_instructions == "yes":
    instructions()
    print()

print("Program Continues")

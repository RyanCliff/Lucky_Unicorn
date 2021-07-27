# Make Function
def yes_no(question):
    valid = False
    while not valid:
        answer = input(question).lower()
        if answer != "yes" and answer != "y":
            print("start game")
            return answer
        elif answer == "no" or answer == "n":
            print("display instructions")
            return answer
        else:
            print("Please pick yes or no.")


# Main Routine
show_instructions = yes_no("Have you played the Lucky Unicorn game before? ")
print("You chose {}".format(show_instructions))

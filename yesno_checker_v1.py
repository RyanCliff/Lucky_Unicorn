answer = input("Have you played the Lucky Unicorn game before?").lower()
if answer == "yes" or "y":
    print("start game")
elif answer == "no" or "n":
    print("display instructions")
else:
    print("Please pick yes or no.")

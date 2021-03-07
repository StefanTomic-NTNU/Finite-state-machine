""" Main file in the Keypad project """
from kpc import KPC


def main():
    """ Main method to run the Keypad project """
    kpc = KPC("password.txt")

    print("                         --- KEYPAD RUNNING --- ")
    print("\nThe keypad is operated with the buttons 0-9, and the letters '#' and '*'.")
    print("In general '#' will cancel an action and return to a standard state.")
    print("Once logged in pressing the letter '#' will lead to logout.")
    print("in general the symbol '*' is used to continue action.")
    print("\nPress any key to continue to login.")

    kpc.do_polling()


# The main function may not be called on an OS other than Windows
if __name__ == "__main__":
    main()

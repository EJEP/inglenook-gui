"""Generate a starting and ending order for a 3-2-2 or 5-3-3 inglenook shunting
puzzle, using TKinter as a gui"""

from random import sample, choice, shuffle, randint
from tkinter import Tk, Label, Button, Entry, StringVar

def get_starting_setup_322(args):
    """Generate the starting positions of the wagons."""

    # Copy the wagons list for convenience
    wagons = args.wagons

    # The long siding can contain either 2 or 3 wagons.
    num_long = randint(2, 3)

    if num_long == 2:
        num_short_1 = 2
        num_short_2 = 2

    if num_long == 3:
        fill_mid = choice([True, False])
        if fill_mid:
            num_short_1 = 2
            num_short_2 = 1
        if not fill_mid:
            num_short_1 = 1
            num_short_2 = 2

    # Randomise the order of the wagons
    shuffle(wagons)

    # Slice the shuffled list to get the wagons to go in each siding
    long_siding = wagons[0:num_long]
    short_1 = wagons[num_long:num_long+num_short_1]
    short_2 = wagons[num_long+num_short_1:]

    print("The starting setup is:")
    print("Long siding:         " + str(long_siding))
    print("First short siding:  " + str(short_1))
    print("Second short siding: " + str(short_2))

def get_starting_setup_533(args):
    """Generate the starting positions of the wagons."""

    wagons = args.wagons
    # First decide where the wagons will go
    # The longest siding must start with between 2 and 5 wagons
    num_long = randint(2, 5)

    # If there are two in the long siding, both the short sidings are full
    if num_long == 2:
        num_short_1 = 3
        num_short_2 = 3

    # If there are three or more wagons in the long siding, then the total
    # number in the short sidings is 8 - num_long
    if num_long >= 3:
        # If there are five wagons in the long siding, mid can have 0 to
        # 3 wagons: minimum of 8 - (num_long + 3)
        # If there are four in the long siding, mid must have at least one
        # wagon in: 8 - (num_long + 3)
        # If there are three in the long siding, mid must have at least two in:
        # 8 - (num_long + 3)

        min_short = 8 - (num_long + 3)
        num_short_1 = randint(min_short, 3)
        num_short_2 = 8 - num_long - num_short_1

    # Randomise the order of the wagons
    shuffle(wagons)

    # Slice the shuffled list to get the wagons to go in each siding
    long_siding = wagons[0: num_long]
    short_1 = wagons[num_long: num_long+num_short_1]
    short_2 = wagons[num_long+num_short_1: ]

    print("The starting setup is:")
    print("Long siding:         " + str(long_siding))
    print("First short siding:  " + str(short_1))
    print("Second short siding: " + str(short_2))

def get_target(wagons, inglenook_type):
    """Set the target train to be assembled. Length depends on the type of
    inglenook"""

    if inglenook_type == '322':
        target = sample(wagons, 4)
    else:
        target = sample(wagons, 5)

    print("The target order is: " + str(target) + '\n')


class Inglenook:

    def __init__(self, master):
        self.master = master
        master.title("Inglenook")

root = Tk()
my_gui = Inglenook(root)
root.mainloop()

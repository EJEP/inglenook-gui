"""Generate a starting and ending order for a 3-2-2 or 5-3-3 inglenook shunting
puzzle, using TKinter as a gui"""

from random import sample, choice, shuffle, randint
from tkinter import Tk, Label, Button, Entry, StringVar, W, E, Radiobutton, IntVar


class Inglenook:

    def __init__(self, master):
        self.master = master
        master.title("Inglenook")

        # Strings to hold the wagon names. Initialise to placeholder values
        # Need 6 wagons for 322 and 8 for 533
        self.wag1 = "A"
        self.wag2 = "B"
        self.wag3 = "C"
        self.wag4 = "D"
        self.wag5 = "E"
        self.wag6 = "F"
        self.wag7 = "G"
        self.wag8 = "H"

        # There are four targets for a 322 and 5 for a 533
        self.targ1 = None
        self.targ2 = None
        self.targ3 = None
        self.targ4 = None
        self.targ5 = None

        self.targ_arr_lab_text = StringVar()
        self.target_arr_label = Label(master, textvariable=self.targ_arr_lab_text)

        self.target_label = Label(master, text="Target arrangement:")

        self.long_lab = Label(master, text="Long siding start:")
        self.start_arr_long_lab_text = StringVar()
        self.start_arr_long_lab = Label(master, textvariable=self.start_arr_long_lab_text)

        self.short1_lab = Label(master, text="First siding start:")
        self.start_arr_short1_lab_text = StringVar()
        self.start_arr_short1_lab = Label(master, textvariable=self.start_arr_short1_lab_text)

        self.short2_lab = Label(master, text="Second siding start:")
        self.start_arr_short2_lab_text = StringVar()
        self.start_arr_short2_lab = Label(master, textvariable=self.start_arr_short2_lab_text)

        # Button to set the type of inglenook.
        # Ready to go once the code works...
        self.ing_type = IntVar()
        self.ing_type.set(533)

        self.ing_332_button = Radiobutton(master, text="322",
                                          variable=self.ing_type,
                                          value=322,
                                          command=self.change_type)
        self.ing_533_button = Radiobutton(master, text="533",
                                          variable=self.ing_type,
                                          value=533,
                                          command=self.change_type)

        # self.entry1 = Entry(master)
        # self.entry2 = Entry(master)
        # self.entry3 = Entry(master)
        # self.entry4 = Entry(master)
        # self.entry5 = Entry(master)
        # self.entry6 = Entry(master)
        # if self.ing_type == 533:
        #     self.entry7 = Entry(master)
        #     self.entry8 = Entry(master)


        self.generate_button = Button(master, text="Generate!", command=self.generate)

        # Layout the buttons
        # self.entry1.grid(row=0, column=0, sticky=W)
        # self.entry2.grid(row=0, column=1, sticky=W)
        # self.entry3.grid(row=0, column=2, sticky=W)
        # self.entry4.grid(row=1, column=0, sticky=W)
        # self.entry5.grid(row=1, column=1, sticky=W)
        # self.entry6.grid(row=1, column=2, sticky=W)

        # if self.ing_type == 533:
        #     self.entry7.grid(row=0, column=3)
        #     self.entry8.grid(row=1, column=3)
        self.draw_boxes()
        self.generate_button.grid(row=2, column=0)

        self.target_label.grid(row=3, column=0, sticky=W)
        self.target_arr_label.grid(row=3, column=1, sticky=W)

        self.long_lab.grid(row=4, column=0, sticky=W)
        self.start_arr_long_lab.grid(row=4, column=1, sticky=W)

        self.short1_lab.grid(row=5, column=0, sticky=W)
        self.start_arr_short1_lab.grid(row=5, column=1, sticky=W)

        self.short2_lab.grid(row=6, column=0, sticky=W)
        self.start_arr_short2_lab.grid(row=6, column=1, sticky=W)

        self.ing_332_button.grid(row=7, column=0)
        self.ing_533_button.grid(row=7, column=1)

    def change_type(self):
        """Change the type of Inglenook to generate for"""

        self.wag1 = "A"
        self.wag2 = "B"
        self.wag3 = "C"
        self.wag4 = "D"
        self.wag5 = "E"
        self.wag6 = "F"
        self.wag7 = "G"
        self.wag8 = "H"

        # There are four targets for a 322 and 5 for a 533
        self.targ1 = None
        self.targ2 = None
        self.targ3 = None
        self.targ4 = None
        self.targ5 = None

        # Update the number of entry boxes
        self.draw_boxes()

        # Reset the target and starting position text.
        self.targ_arr_lab_text.set('')
        self.start_arr_long_lab_text.set('')
        self.start_arr_short1_lab_text.set('')
        self.start_arr_short2_lab_text.set('')


    def draw_boxes(self):
        """Draw the entry boxes for the wagons"""

        self.entry1 = Entry(self.master)
        self.entry2 = Entry(self.master)
        self.entry3 = Entry(self.master)
        self.entry4 = Entry(self.master)
        self.entry5 = Entry(self.master)
        self.entry6 = Entry(self.master)
        if self.ing_type.get() == 533:
            self.entry7 = Entry(self.master)
            self.entry8 = Entry(self.master)

        # Layout the buttons
        self.entry1.grid(row=0, column=0, sticky=W)
        self.entry2.grid(row=0, column=1, sticky=W)
        self.entry3.grid(row=0, column=2, sticky=W)
        self.entry4.grid(row=1, column=0, sticky=W)
        self.entry5.grid(row=1, column=1, sticky=W)
        self.entry6.grid(row=1, column=2, sticky=W)

        # Show two extra text fields if a 533 is selected.
        if self.ing_type.get() == 533:
            self.entry7.grid(row=0, column=3)
            self.entry8.grid(row=1, column=3)
        # Hide them if not
        if self.ing_type.get() == 322:
            self.entry7.grid_remove()
            self.entry8.grid_remove()


    def generate(self):
        """Generate the start and end positions"""
        self.get_wags()
        self.get_target()
        if self.ing_type.get() == 322:
            self.get_starting_setup_322()
        else:
            self.get_starting_setup_533()


    def get_wags(self):
        """Get the entered wagons"""

        # This maybe could be in a validate function?
        if self.entry1.get() is not '':
            self.wag1 = self.entry1.get()
        if self.entry2.get() is not '':
            self.wag2 = self.entry2.get()
        if self.entry3.get() is not '':
            self.wag3 = self.entry3.get()
        if self.entry4.get() is not '':
            self.wag4 = self.entry4.get()
        if self.entry5.get() is not '':
            self.wag5 = self.entry5.get()
        if self.entry6.get() is not '':
            self.wag6 = self.entry6.get()

        if self.ing_type.get() == 533:
            if self.entry7.get() is not '':
                self.wag7 = self.entry7.get()
            if self.entry8.get() is not '':
                self.wag8 = self.entry8.get()


    def get_target(self):
        """Set the target train to be assembled. Length depends on the type of
        inglenook"""

        #wagons = [self.wag1, self.wag2, self.wag3, self.wag4, self.wag5,
        #          self.wag6]
        #target = sample(wagons, 4)
        # self.targ1 = target[0]
        # self.targ2 = target[1]
        # self.targ3 = target[2]
        # self.targ4 = target[3]


        # Might work to set up different types...
        if self.ing_type.get() == 322:
            wagons = [self.wag1, self.wag2, self.wag3,
                      self.wag4, self.wag5, self.wag6]
            target = sample(wagons, 4)
            self.targ1 = target[0]
            self.targ2 = target[1]
            self.targ3 = target[2]
            self.targ4 = target[3]

        else:
            wagons = [self.wag1, self.wag2, self.wag3, self.wag4,
                      self.wag5, self.wag6, self.wag7, self.wag8]
            target = sample(wagons, 5)
            self.targ1 = target[0]
            self.targ2 = target[1]
            self.targ3 = target[2]
            self.targ4 = target[3]
            self.targ5 = target[4]

        self.targ_arr_lab_text.set(', '.join(target))


    def get_starting_setup_322(self):
        """Generate the starting positions of the wagons."""

        wagons = [self.wag1, self.wag2, self.wag3, self.wag4, self.wag5,
                  self.wag6]

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

        self.start_arr_long_lab_text.set(', '.join(long_siding))
        self.start_arr_short1_lab_text.set(', '.join(short_1))
        self.start_arr_short2_lab_text.set(', '.join(short_2))

    def get_starting_setup_533(self):
        """Generate the starting positions of the wagons."""

        wagons = [self.wag1, self.wag2, self.wag3, self.wag4,
                  self.wag5, self.wag6, self.wag7, self.wag8]
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
            # If there are five wagons in the long siding, mid can have 0 to 3
            # wagons: minimum of 8 - (num_long + 3) If there are four in the
            # long siding, mid must have at least one wagon in:
            # 8 - (num_long + 3)
            # If there are three in the long siding, mid must have at least
            # two in:
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

        self.start_arr_long_lab_text.set(', '.join(long_siding))
        self.start_arr_short1_lab_text.set(', '.join(short_1))
        self.start_arr_short2_lab_text.set(', '.join(short_2))


root = Tk()
my_gui = Inglenook(root)
root.mainloop()

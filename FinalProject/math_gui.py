"""
Program: math_gui.py
Author: Jonathan Neff
Last date modified: 10/27/2023

The purpose of this program is provide the user interface for the math game
"""

import tkinter
import tkinter.messagebox
import math_class as mc

class MathGame:

    def __init__(self):
        self.COLUMN_SPAN = 6
        self.math_class = mc.MathClass()
        self.math_problem = ""
        self.welcome_screen()
        return

    def reset_game(self):
        self.math_class.reset_the_game()
        return

    def submit_answer(self):
        math_class.submit_answer
        math_problem = self.math_class.get_problem()
        math_operation = self.math_class.math_operation
        math_output = str(math_problem[0]) + " " + math_operation + " " + str(math_problem[1])
        label = self.math_problem
        label.config(text=math_output)
        return

    def welcome_screen(self):
        self.m = tkinter.Tk()  # where m is the name of the main window object
        self.m.title("Math Game")

        welcome_label = tkinter.Label(self.m, text="Welcome To The Math Game!")
        welcome_label.configure(font=("Helvetica", 10, "bold"))
        welcome_label.grid(columnspan=self.COLUMN_SPAN, row=1)

        #  Start Button
        start_button = tkinter.Button(self.m, text='Start Game', width=50, command=self.m.destroy)
        start_button.grid(columnspan=self.COLUMN_SPAN, row=2)

        self.m.mainloop()  # infinite loop that waits for events to happen
        self.initialize_GUI()

    def initialize_GUI(self):
        self.reset_game()
        self.m = tkinter.Tk()  # where m is the name of the main window object
        self.m.title("Math Game")

        row = 0
        welcome_label = tkinter.Label(self.m, text="Welcome To Math Fun!")
        welcome_label.configure(font=("Helvetica", 10, "bold"))

        row += 1
        welcome_label.grid(columnspan=self.COLUMN_SPAN, row=row)

        row += 1
        tkinter.Label(self.m, text="Question:").grid(column=0, row=row)

        # output the first math problem
        math_problem = self.math_class.get_problem()
        math_operation = self.math_class.math_operation
        math_output = str(math_problem[0]) + " " + math_operation + " " + str(math_problem[1])
        self.math_problem = tkinter.Label(self.m, text=str(math_output))
        self.math_problem.grid(column=1, row=row)

        #   Fields
        row += 1
        tkinter.Label(self.m, text="What is your answer?").grid(column=0, row=row)
        math_answer = tkinter.Entry(self.m)
        math_answer.grid(column=1, row=row)

        #  Reset Button
        row += 1
        submit_button = tkinter.Button(self.m, text='Submit Answer', width=50, command=lambda: self.submit_answer())
        submit_button.grid(columnspan=self.COLUMN_SPAN, row=row)

        #  Submit Button
        row += 1
        reset_button = tkinter.Button(self.m, text='Reset', width=50, command=lambda: self.reset_game())
        reset_button.grid(columnspan=self.COLUMN_SPAN, row=row)

        #  Exit Button
        row += 1
        exit_button = tkinter.Button(self.m, text='Exit', width=50, command=self.m.destroy)
        exit_button.grid(columnspan=self.COLUMN_SPAN, row=row)

        self.m.mainloop()  # infinite loop that waits for events to happen


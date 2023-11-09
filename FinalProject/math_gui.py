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
        try:
            answer = int(self.math_answer.get())
        except ValueError:
            tkinter.messagebox.showerror(title="Error", message="Answer must be a number")
            return
        is_correct = self.math_class.submit_answer(answer)
        if is_correct:
            self.is_correct_label.configure(text="Correct!")
            self.is_correct_label.configure(fg="green")
        else:
            self.is_correct_label.configure(text="Incorrect")
            self.is_correct_label.configure(fg="red")

        self.math_answer.config(state="readonly")
        if self.math_class.questions_asked == self.math_class.NUMBER_OF_QUESTIONS:
            self.submit_button.config(text="View Results", command=lambda: self.view_results())
        else:
            self.submit_button.config(text="Next Question", command=lambda: self.next_question())
        return

    def next_question(self):
        self.math_answer.config(state="normal")
        self.submit_button.config(text="Submit Answer", command=lambda: self.submit_answer())
        self.math_answer.delete(0, "end")
        self.is_correct_label.configure(text="")
        math_problem = self.math_class.get_problem()
        math_operation = self.math_class.math_operation
        math_output = str(math_problem[0]) + " " + math_operation + " " + str(math_problem[1])
        label = self.math_problem
        label.config(text=math_output)

    def view_results(self):
        self.m = tkinter.Tk()  # where m is the name of the main window object
        self.m.title("Results")

        welcome_label = tkinter.Label(self.m, text="Results:")
        welcome_label.configure(font=("Helvetica", 10, "bold"))
        welcome_label.grid(columnspan=self.COLUMN_SPAN, row=1)



        self.m.mainloop()  # infinite loop that waits for events to happen
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
        column = 0
        tkinter.Label(self.m, text="Question:").grid(column=column, row=row)

        # output the first math problem
        column = column + 1
        math_problem = self.math_class.get_problem()
        math_operation = self.math_class.math_operation
        math_output = str(math_problem[0]) + " " + math_operation + " " + str(math_problem[1])
        self.math_problem = tkinter.Label(self.m, text=str(math_output))
        self.math_problem.grid(column=column, row=row)

        #   Fields
        row += 1
        column = column + 1
        tkinter.Label(self.m, text="What is your answer?").grid(column=0, row=row)
        self.math_answer = tkinter.Entry(self.m)
        self.math_answer.grid(column=1, row=row)
        self.is_correct_label = tkinter.Label(self.m, text="")
        self.is_correct_label.grid(column=column, row=row)
        self.is_correct_label.configure(font=("Helvetica", 10, "bold"))

        #  Submit Button
        row += 1
        self.submit_button = tkinter.Button(self.m, text='Submit Answer', width=50, command=lambda: self.submit_answer())
        self.submit_button.grid(columnspan=self.COLUMN_SPAN, row=row)

        #  Reset Button
        row += 1
        reset_button = tkinter.Button(self.m, text='Reset', width=50, command=lambda: self.reset_game())
        reset_button.grid(columnspan=self.COLUMN_SPAN, row=row)

        #  Exit Button
        row += 1
        exit_button = tkinter.Button(self.m, text='Exit', width=50, command=self.m.destroy)
        exit_button.grid(columnspan=self.COLUMN_SPAN, row=row)

        self.m.mainloop()  # infinite loop that waits for events to happen


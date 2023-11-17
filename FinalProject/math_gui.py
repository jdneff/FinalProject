"""
Program: math_gui.py
Author: Jonathan Neff
Last date modified: 11/10/2023

The purpose of this program is provide the user interface for the math game
"""

import tkinter
import tkinter.messagebox
import math_class as mc

class MathGame:

    def __init__(self):
        self.COLUMN_SPAN = 6
        # math class controls functions outside the scope of GUI and interfaces with math_queue and math_answers
        self.math_class = mc.MathClass()
        # initialize the main tkinter window
        self.m = tkinter.Tk()
        # load the welcome screen
        self.welcome_screen()
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
        if self.math_class._questions_asked == self.math_class._number_of_questions:
            self.submit_button.config(text="View Results", command=self.view_results)
        else:
            self.submit_button.config(text="Next Question", command=self.next_question)
        return

    def next_question(self):
        self.math_answer.config(state="normal")
        self.submit_button.config(text="Submit Answer", command=self.submit_answer)
        self.math_answer.delete(0, "end")
        self.is_correct_label.configure(text="")
        math_problem = self.math_class.get_problem()
        math_operation = self.math_class._math_operation
        math_output = str(math_problem[0]) + " " + math_operation + " " + str(math_problem[1])
        label = self.math_problem
        label.config(text=math_output)

    def welcome_screen(self):

        # destroy all items from previous "screen"
        for item in self.m.grid_slaves():
            item.destroy()

        self.m.title("Math Game")

        # welcome label
        row = 0
        welcome_label = tkinter.Label(self.m, text="Welcome To The Math Game!")
        welcome_label.configure(font=("Helvetica", 10, "bold"))
        welcome_label.grid(columnspan=self.COLUMN_SPAN, row=row)

        row = row + 1
        column = 1
        number_of_questions_label = tkinter.Label(self.m, text="How many questions? (1-10)")
        number_of_questions_label.grid(column=column, row=row)
        column = column + 1
        self.number_of_questions_input = tkinter.Entry(self.m)
        self.number_of_questions_input.grid(column=2, row=row)

        # Addition button
        row = row + 1
        tkinter.Button(self.m, text="Addition", width=50, command=lambda: self.start_game("Addition")).\
            grid(columnspan=self.COLUMN_SPAN, row=row)

        # Subtraction button
        row = row + 1
        tkinter.Button(self.m, text="Subtraction", width=50, command=lambda: self.start_game("Subtraction")).\
            grid(columnspan=self.COLUMN_SPAN, row=row)

        # Multiplication button
        row = row + 1
        tkinter.Button(self.m, text="Multiplication", width=50, command=lambda: self.start_game("Multiplication")).\
            grid(columnspan=self.COLUMN_SPAN, row=row)

        # Division Button
        row = row + 1
        tkinter.Button(self.m, text="Division", width=50, command=lambda: self.start_game("Division")).\
            grid(columnspan=self.COLUMN_SPAN, row=row)

        #  Exit Button
        row += 1
        exit_button = tkinter.Button(self.m, text='Exit', width=50, command=self.m.destroy)
        exit_button.grid(columnspan=self.COLUMN_SPAN, row=row)

        self.number_of_questions_input.focus_set()
        self.m.mainloop()  # infinite loop that waits for events to happen

    def start_game(self, game_mode):
        MAX_QUESTIONS = 10
        try:
            number_of_questions = int(self.number_of_questions_input.get())
            if number_of_questions < 1 or number_of_questions > MAX_QUESTIONS:
                tkinter.messagebox.showerror(title="Error", message="Please enter a value between 1 and " + str(MAX_QUESTIONS))
                return
        except ValueError:
            tkinter.messagebox.showerror(title="Error", message="Please enter a value between 1 and " + str(MAX_QUESTIONS))
            return

        # destroy all items from previous "screen"
        for item in self.m.grid_slaves():
            item.destroy()

        self.m.title("Math Game")
        self.math_class.start_the_game(game_mode, number_of_questions)

        row = 0
        column = 0
        tkinter.Label(self.m, text="Question:").grid(column=column, row=row)

        # output the first math problem
        column = column + 1
        math_problem = self.math_class.get_problem()
        math_operation = self.math_class._math_operation
        math_output = str(math_problem[0]) + " " + math_operation + " " + str(math_problem[1])
        self.math_problem = tkinter.Label(self.m, text=str(math_output))
        self.math_problem.grid(column=column, row=row)
        self.math_problem.configure(font=("Helvetica", 12, "bold"))

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
        self.submit_button = tkinter.Button(self.m, text='Submit Answer', width=50, command=self.submit_answer)
        self.submit_button.grid(columnspan=self.COLUMN_SPAN, row=row)

        #  Reset Button
        row += 1
        reset_button = tkinter.Button(self.m, text='Reset', width=50, command=self.welcome_screen)
        reset_button.grid(columnspan=self.COLUMN_SPAN, row=row)

        #  Exit Button
        row += 1
        exit_button = tkinter.Button(self.m, text='Exit', width=50, command=self.m.destroy)
        exit_button.grid(columnspan=self.COLUMN_SPAN, row=row)

        self.math_answer.focus_set()
        self.m.mainloop()  # infinite loop that waits for events to happen

    def view_results(self):
        # destroy all items from previous "screen"
        for item in self.m.grid_slaves():
            item.destroy()
        self.m.title("Results")
        COLUMN_SPAN = 5

        row = 0
        column = 1
        # question header
        question_label = tkinter.Label(self.m, text="Question")
        question_label.grid(column=column, row=row)
        question_label.configure(font=("Helvetica", 10, "bold"))
        column = column + 1
        # answer header
        answer_label = tkinter.Label(self.m, text="Answer")
        answer_label.grid(column=column, row=row)
        answer_label.configure(font=("Helvetica", 10, "bold"))
        column = column + 1
        # result header
        result_label = tkinter.Label(self.m, text="Result")
        result_label.grid(column=column, row=row)
        result_label.configure(font=("Helvetica", 10, "bold"))

        while self.math_class._math_answers.size() > 0:
            row = row + 1
            column=1
            item = self.math_class.get_next_answer()

            # output the math problem
            problem = str(item._problem[0]) + item._operation + str(item._problem[1])
            tkinter.Label(self.m, text=problem).grid(column=column, row=row)
            column = column + 1

            #output answer
            tkinter.Label(self.m, text=item._answer).grid(column=column, row=row)
            column = column + 1

            # output correct/incorrect
            is_correct = "Incorrect"
            text_color = "red"
            if item._is_correct:
                is_correct = "Correct!"
                text_color = "green"
            correct_label = tkinter.Label(self.m, text=is_correct, fg=text_color)
            correct_label.grid(column=column, row=row)
            correct_label.configure(font=("Helvetica", 10, "bold"))


        #  Reset Button
        row += 1
        restart_button = tkinter.Button(self.m, text='Reset', width=50, command=self.welcome_screen)
        restart_button.grid(columnspan=COLUMN_SPAN, row=row)

        #  Exit Button
        row += 1
        exit_button = tkinter.Button(self.m, text='Exit', width=50, command=self.m.destroy)
        exit_button.grid(columnspan=COLUMN_SPAN, row=row)

        self.m.mainloop()  # infinite loop that waits for events to happen
        return


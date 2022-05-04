import tkinter as tk
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(background=THEME_COLOR, pady=20, padx=20)
        self.canvas = tk.Canvas(width=300, height=350)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(150, 175, width=250, text='HI! This is a starting point',
                                                     font=('Arial', 20, 'italic'))
        self.next_question()

        self.false_image = tk.PhotoImage(file='images/false.png')
        self.false_button = tk.Button(image=self.false_image, command=self.false_func)
        self.false_button.grid(row=2, column=0)

        self.true_image = tk.PhotoImage(file='images/true.png')
        self.true_button = tk.Button(image=self.true_image, command=self.true_func)
        self.true_button.grid(row=2, column=1)

        self.score = tk.Label(text=f'Score: {self.quiz.score}', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

    def next_question(self):
        self.window.after(1000, self.canvas.config(bg='white'))
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text=f'Game is over\n'
                                                            f'Your score is {self.quiz.score}/{self.quiz.question_number}')
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')

    def check_answer(self, user_answer):
        if self.quiz.check_answer(user_answer) == True:
            self.canvas.config(bg='green')
            self.window.update()
        else:
            self.canvas.config(bg='red')
            self.window.update()
        self.score.config(text=f'Score: {self.quiz.score}/{self.quiz.question_number}')

    def true_func(self):
        user_answer = 'True'
        self.check_answer(user_answer)
        self.next_question()

    def false_func(self):
        user_answer = 'False'
        self.check_answer(user_answer)
        self.next_question()

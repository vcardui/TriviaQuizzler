from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"
TEXT_CONFIG = ("Arial", 20, "italic")
SCORE_CONFIG = ("Arial", 15)
WHITE = "#FFFFFF"
GREEN = "#62BD69"
RED = "#FF0000"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Trivia Time!")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_text = Label(text="Score: 0", font=SCORE_CONFIG, fg=WHITE, bg=THEME_COLOR)
        self.score_text.grid(column=1, row=0)
        self.score_text.place(x=275, y=1, anchor=CENTER)

        self.question_canvas = Canvas(width=300, height=250, bg=WHITE, highlightthickness=0)
        self.question_text = self.question_canvas.create_text(
            150,
            125,
            width=200,
            text="Some Question Text",
            font=TEXT_CONFIG,
            fill=THEME_COLOR)
        self.question_canvas.grid(column=0, row=1, columnspan=2, padx=(10, 10), pady=(40, 40))

        self.false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_img, bg=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.false_pressed)
        self.false_button.grid(column=0, row=2, padx=(20, 20), pady=(10, 10))

        self.true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img, bg=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=2, padx=(20, 20), pady=(10, 10))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg=WHITE)
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text=f"You have completed all the questions.\nYour final score is\n{self.quiz.score}/10")
            self.true_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.show_answer(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.show_answer(is_right)

    def show_answer(self, is_right):
        if is_right:
            self.question_canvas.config(bg=GREEN)
        else:
            self.question_canvas.config(bg=RED)

        self.window.after(1000, self.get_next_question)



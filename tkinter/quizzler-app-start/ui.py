from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        """Initializes the QuizInterface with a QuizBrain instance."""
        """Sets up the GUI components for the quiz application."""
        """Creates the main window, score label, canvas for question text, and buttons."""
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text...",
            fill="black",
            font=("Arial", 20, "italic"),
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_image = PhotoImage(file="tkinter/quizzler-app-start/images/true.png")
        self.true_button = Button(
            image=true_image,
            highlightthickness=0,
            command=self.true_pressed,
        )
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="tkinter/quizzler-app-start/images/false.png")
        self.false_button = Button(
            image=false_image,
            highlightthickness=0,
            command=self.false_pressed,
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.canvas.question_text, text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        """Handles the event when the 'True' button is pressed."""
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        """Handles the event when the 'False' button is pressed."""
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        """Provides feedback by changing the background color based on the user's answer."""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # Delay the next question to allow feedback to be visible
        self.window.after(1000, self.get_next_question)

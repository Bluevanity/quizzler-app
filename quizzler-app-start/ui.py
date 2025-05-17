from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox

THEME_COLOR = "#375362"
FONT= ("Arial", 20, "italic")

class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.message = messagebox

        self.window= Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas= Canvas(width=400, height=350, bg="white")
        self.question_text= self.canvas.create_text( 200, 175, width=280, text="Something about quiz", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=30, pady=30)
        
        self.score= Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        wrong_image= PhotoImage(file="images/false.png")
        self.button_bad= Button(image=wrong_image, highlightthickness=0, bg=THEME_COLOR, pady=50, command=self.bad_press)
        self.button_bad.grid(row=2, column=1)
        
        right_image= PhotoImage(file="images/true.png")
        self.button_good= Button(image=right_image, highlightthickness=0, bg=THEME_COLOR, pady=50, command=self.good_press)
        self.button_good.grid(row=2, column=0)
        
        self.to_next()

        self.window.mainloop()
    
    def to_next(self):
        self.canvas.config(bg= "white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            messagebox.showinfo("CONGRATULATIONS", F"This quiz has come to an end\nYour score is {self.quiz.score}/{self.quiz.question_number}")
            self.button_good.config(state="disabled")
            self.button_bad.config(state="disabled")  

    def good_press(self):
       self.give_feedback(self.quiz.check_answer("true"))
    
    def bad_press(self):
       self.give_feedback(self.quiz.check_answer("false"))
    
    def give_feedback(self, is_right):
        self.window.after_cancel(self.to_next)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.to_next)
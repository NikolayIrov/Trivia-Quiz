import quiz_brain
import ui
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui=ui.QuizInterface(quiz)

while quiz_ui.quiz.still_has_questions():
    quiz_ui.window.mainloop()
# while quiz.still_has_questions():
#     quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {quiz_ui.score_val}/{quiz.question_number}")

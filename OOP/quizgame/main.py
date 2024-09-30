from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

    if not quiz.still_has_questions():
        print("You have completed the quiz!")
        print(f"Your final score is: {quiz.user_score}/{quiz.question_number}")

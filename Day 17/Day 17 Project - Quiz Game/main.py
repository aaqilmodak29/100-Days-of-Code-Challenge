from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # retrieving question from question_data
    question_text = question["question"]
    # retrieving answer from question_data
    question_answer = question["correct_answer"]
    # creating object new_q from class Question that accepts the question and answer retrieved above
    new_q = Question(question_text, question_answer)
    # appending the question and answer to an empty list question_bank
    question_bank.append(new_q)

set_of_q = QuizBrain(question_bank)

while set_of_q.still_has_questions():
    set_of_q.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {set_of_q.score}/{set_of_q.question_number}")

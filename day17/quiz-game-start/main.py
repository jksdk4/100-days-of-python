from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import random

question_bank = []
random_quiz = random.choice(question_data)

for question in random_quiz:
    q_text = question["text"]
    q_answer = question["answer"]
    q_type = question["type"]
    if "incorrect_answers" in question.keys():
        q_choices = question["incorrect_answers"]
        new_question = Question(q_text, q_answer, q_type, q_choices)
    else:
        new_question = Question(q_text, q_answer, q_type)
    question_bank.append(new_question)  # it's ok that they're obj addresses, u can still access props

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"\nFinal score: {quiz.score}/{quiz.question_num}")

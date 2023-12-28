import random


class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_num]
        t_or_f = " True or False -" if current_q.q_type == "boolean" else ""
        self.question_num += 1

        print(f'Q{self.question_num}:{t_or_f} {current_q.text} ')
        if current_q.q_type == "multiple":
            current_q.choices.append(current_q.answer)
            random.shuffle(current_q.choices)
            for choice in current_q.choices:
                print(f"- {choice}")

        user_answer = input('>> ')
        self.check_answer(user_answer, current_q.answer)

    def still_has_questions(self):
        # if self.question_num >= len(self.question_list):
        #     return False
        # return True

        # or, you could do this
        # since the question_num increases, you could just see if it reaches the len.
        # because once question_num hits num of imported qs, it'd match the len of the list and be false.
        return self.question_num < len(self.question_list)

    def check_answer(self, user_ans, question_ans):
        if user_ans.lower() == question_ans.lower():
            self.score += 1
            print(f"\nYes, that's right.")
        else:
            print(f"\nNo, it's {question_ans}.")
        print(f"Current Score: {self.score}/{self.question_num} right.\n")

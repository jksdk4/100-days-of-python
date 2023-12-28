class Question:
    def __init__(self, text, answer, q_type, choices=None):
        self.text = text
        self.answer = answer
        self.q_type = q_type
        self.choices = choices


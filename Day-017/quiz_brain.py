class QuizBrain:


    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):

        question = self.question_list[self.question_number]
        self.question_number += 1
        resp = input(f"Q.{self.question_number}:  {question.text} (True/False)\n > ").lower()
        self.check_answer(resp, question.answer)


    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That's Right")
        else:
            print("Sorry, wrong answer")

        print(f"Your current score {self.score}/{self.question_number}")
        print()


    def still_has_questions(self):

        if self.question_number < len(self.question_list):
            return True

        return False

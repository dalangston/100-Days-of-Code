from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


if __name__ == '__main__':

    question_bank = []

    for d in question_data:
        question_bank.append(Question(d['text'], d['answer']))
        #question_bank.append(Question(d['question'], d['correct_answer']))

    quiz_brain = QuizBrain(question_bank)

    while quiz_brain.still_has_questions():
        quiz_brain.next_question()

    print()
    print("You've completed the quiz!")
    print(f"Your final score was:  {quiz_brain.score}/{len(question_bank)}")

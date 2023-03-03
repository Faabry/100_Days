class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    
    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        return True


    def next_question(self):
        # The self.question_list[index of self.question_number]
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} True/False: ").title()
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right! ")
        else:
            print("You got ir wrong!")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("")
        
    
class QuizBrain:
    def __init__(self, list_of_questions):
        """
        called when object is created from this class
        :param list_of_questions: accepts question bank as a list
        """
        self.question_number = 0
        self.score = 0
        self.question_list = list_of_questions
        # print(self.question_list[0].answer)

    def still_has_questions(self):
        """
        checks if there are still any questions in the question bank, if not, returns false.
        :return: returns a boolean value
        """
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        """
        goes to the next question and increments question number by 1
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, right_answer):
        """
        if user's answer matches the right answer, increment score by 1
        :param user_answer: the answer that the user inputs
        :param right_answer: the correct answer given in question bank
        """
        if user_answer.lower() == right_answer.lower():
            print("Correct")
            self.score += 1
            print(f"Your score is: {self.score}/{self.question_number}")
            print("\n")

        else:
            print("Wrong")
            print(f"Your score is: {self.score}/{self.question_number}")
            print("\n")

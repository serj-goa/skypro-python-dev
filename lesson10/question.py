class Question:
    def __init__(self, text_question: str, diff_question: str, corr_answer: str) -> None:
        self.text_question = text_question  # текст вопроса
        self.diff_question = diff_question  # сложность вопроса
        self.corr_answer = corr_answer  # верный вариант ответа
        self.points_by_question = self.get_points()  # баллы за вопрос

        self.ask_question = False  # задан ли вопрос
        self.player_answer = None  # ответ пользователя

    def get_points(self):
        """
        It calculates the number of points for the question.
        """
        return int(self.diff_question) * 10

    def is_correct(self):
        """
        Checks if the player's answer matches the correct answer.
        """
        return self.player_answer == self.corr_answer

    def build_question(self):
        """
        Forms a question to the player.
        """
        return f'Вопрос: {self.text_question}\nСложность {self.diff_question}/5'

    def build_feedback(self):
        """
        Generates a response to the player depending on the correctness of the answer.
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.points_by_question} баллов\n'

        return f'Ответ неверный, верный ответ {self.corr_answer}\n'

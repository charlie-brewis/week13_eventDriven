class Question:

    def __init__(self, question, answer):
        
        self.question = question
        self.answer = answer

    def getQuestion(self):
        return self.question

    def checkAnswer(self, userAnswer):
        return self.answer == userAnswer


class Quiz:
    
    def __init__(self):
        self.questions = []

    def addQuestion(self, question, answer):
        newQuestion = Question(question, answer)
        self.questions.append(newQuestion)

    def removeQuestionAt(self, index):
        del self.questions[index]

    def getQuestionAt(self, index):
        return self.questions[index].getQuestion()

    def checkAnswerAt(self, index, userAnswer):
        return self.questions[index].checkAnswer(userAnswer)

    def getNumQuestions(self):
        return len(self.questions)
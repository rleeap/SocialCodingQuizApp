class calculateScore:
    def __init__(self, ID, score):
        self.user = ID
        self.score = 0

    def getScore(self):
        return self.score

    #This calculates the score of each user.
    def setScore(self, score):
        self.score += score

    def quizDisplay(user, quiz, answer):
        for i in range(quiz):
            print(quiz[i])
            answer = input("Answer: ")

            #If the answer is the equal with the quiz,
            #Add the score
            if (answer[i] == answer):
                setScore(user, 1)
        print("Your score is " + getScore)
        

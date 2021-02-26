

def displayQuestion(questionText, answers, correctAnswerNumber):
    # questionText: text that will be displayed
    # answers: array of possible answers to the question
    # correctAnswerNumber: index of the correct answer (1-indexed)
    # returns 1 for correct and 0 for incorrect

    print(questionText)
    for x in range (0, len(answers)):
        print(str(x + 1) + ". " + answers[x])
    userAnswer = input("My guess: ")
    if (userAnswer == correctAnswerNumber):
        return 1 
    return 0


# example usage
# displayQuestion("what is the first letter of the alphabet?", ["a", "b", "c", "d"], 1)



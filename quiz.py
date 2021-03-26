def startQuiz():
    while (True):
        print("Start Quiz")
        num_questions = howManyQuestions("samplequiz.txt") #count number of quesitons in the file.
        answers = displayQuestion("samplequiz.txt") #display the question.
        
        
        num_correct = checkAnswers("samplequiz.txt", answers) #check num of correct answersa
        final_score = calculateScore(num_correct, num_questions) #calculate final score
        print("Your Final Score is: {}%".format(final_score)) 
        #shows a comparison between your answer and the correct answer 
        compareAnswers("samplequiz.txt", answers)
        again = input("Restart? Y/N\n")
        if (again == "N" or again == "n"):
            break

#Function that takes in a quiz file and returns a list filled with the correct answers sequentially listed
def getCorrectAnswers(filename):
    fileObject = open(filename, 'r')
    num_questions = int(fileObject.readline())
    answer_lines = fileObject.readlines()[num_questions*2+1:]
    for i in range(len(answer_lines)):
        answer_lines[i] = answer_lines[i].strip('\n').strip()
    fileObject.close()
    return answer_lines

#Function to print a comparison between your answer and the correct answer
def compareAnswers(filename, answers):
    correct_answer = getCorrectAnswers(filename)
    print("Your Answer \t Correct Answer\n")
    for i in range(len(correct_answer)):
        print ("{} \t\t {}\n".format(answers[i], correct_answer[i]))
    
#Function to get the number of question in the quiz file.
def howManyQuestions(filename):
    fileObject = open(filename, 'r')
    num_lines = int(fileObject.readline())
    fileObject.close()
    return num_lines

#Function that displays the question in the quiz file
def displayQuestion(filename):
    answers = []
    j = 0
    fileObject = open(filename, 'r')
    num_questions = int(fileObject.readline())
    for i in range(num_questions*2):
        print(fileObject.readline())
        #If i is odd number, it asks users to answer the question.
        if (i % 2 == 1):
            answers.append(input("Your answer for question {}:\n".format(j+1)))
            j += 1
    fileObject.close()
    return answers

#Function to check the answers and returns the number of correct answer
def checkAnswers(filename, answer_list):
    num_correct = 0
    correct_answers = getCorrectAnswers(filename)
    for i in range(len(correct_answers)):
        if correct_answers[i] == answer_list[i]:
            num_correct += 1
    return num_correct

#Returns the total percentage score
def calculateScore(correct, total_questions):
    return round(correct/total_questions * 100, 2)

#It is the function to get the answer from the user.
def getQuestions(answers, j):
    answers.append(input("Your answer for question {}:\n".format(j+1)))


startQuiz()

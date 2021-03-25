#Function to check the answers and returns the number of correct answer
def checkAnswers(filename, answer_list):
    num_correct = 0
    correct_answers = getCorrectAnswers(filename)
    for i in range(len(correct_answers)):
        if correct_answers[i] == answer_list[i]:
            num_correct += 1
    return num_correct
    
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
    fileObject = open(filename, 'r')
    num_questions = int(fileObject.readline())
    for i in range(num_questions*2):
        print(fileObject.readline())
    fileObject.close()

#Returns the total percentage score
def calculateScore(correct, total_questions):
    return round(correct/total_questions * 100, 2)

def getUserAnswers(num_questions):
    questions_left = num_questions
    curr_question = 1
    user_answers = []
    while questions_left != 0:
        answer = input("Enter answer for Q({}):\n".format(curr_question))
        #keep on asking user for answer if their answer is not A, B, C or D
        while (answer != 'A' and answer != 'B' and answer != 'C' and answer != 'D'):
            answer = input("Answer invalid. Please try again: \n")
        user_answers.append(answer)
        curr_question += 1
        questions_left -= 1
    return user_answers

def startQuiz():
    while (True):
        print("Start Quiz")

        num_questions = howManyQuestions("samplequiz.txt") #count number of questions in the file.
        displayQuestion("samplequiz.txt")

        #would be a list that contains user answers.
        answers = getUserAnswers(num_questions)
        num_correct = checkAnswers("samplequiz.txt", answers) #check num of correct answers

        final_score = calculateScore(num_correct, num_questions) #calculate final score
        print("Your Final Score is: {}%".format(final_score)) 

        #shows a comparison between your answer and the correct answer 
        compareAnswers("samplequiz.txt", answers)
        again = input("Restart? Y/N\n")
        while (again != 'Y' and again != 'y' and again != 'N' and again != 'n'):
            again = input("Invalid. Try again: \n")
        if (again == "N" or again == "n"):
            break

def main():
    startQuiz()

if __name__ == '__main__':
    main()

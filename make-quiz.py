def makeQuiz():
  print("Make Quiz")
  quiz_name = input("Enter quiz name: ") + ".txt" #Ask for name of new quiz file
  quiz_file = open(quiz_name, "w+") #Create .txt file with given name
  num_questions = 0
  while (True):
    
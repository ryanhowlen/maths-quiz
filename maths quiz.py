import random


def multiple_choice():
  score = 0
  m_questions = ['What is 12 + 11?', 'What is the square of 5?', 'Is 59 a prime number?'] #list of questions
  m_correct = ['2', '3', '1'] #list of correct answers
  m_answers = [['10'], ['23'], ['32']], [['22'], ['34'], ['25']], [['Yes'], ['No']] #list of possible answers to choose from
  
  
  random.shuffle(m_questions)#shuffles the question list so that questions are chosen at random

  
  while len(m_questions) > 0: #the loop will end when the question list is empty
    if m_questions[0] == 'What is 12 + 11?':
      print (m_questions[0])
      print ('\n1.', m_answers[0][0], '\n2.', m_answers[0][1], '\n3.', m_answers[0][2], '\n')
      choice = str(input("Enter a number for your choice: "))
      if choice == m_correct[0]:
        print("Correct!")
        score += 1
        del m_questions[0] #removes the question that was just asked from the list of questions
      

      else:
        print ("incorrect")
        del m_questions[0]
    
    elif m_questions[0] == 'What is the square of 5?':
      print (m_questions[0])
      print ('\n1.', m_answers[1][0], '\n2.', m_answers[1][1], '\n3.', m_answers[1][2], '\n')
      choice = str(input("Enter a number for your choice: "))
      if choice == m_correct[1]:
        print("Correct!")
        score += 1
        del m_questions[0]
      
      else:
        print ("incorrect")
        del m_questions[0]
    
    elif m_questions[0] == 'Is 59 a prime number?':
      print (m_questions[0])
      print ('\n1.', m_answers[2][0], '\n2.', m_answers[2][1], '\n')
      choice = str(input("Enter a number for your choice: "))
      if choice == m_correct[2]:
        print("Correct!")
        score += 1
        del m_questions[0]
      
      else:
        print ("incorrect")
        del m_questions[0]
  print ("Your Score is:", score)
  

def general_answer():
  score = 0 
  g_questions = ['What is 12 + 11?', 'What is the square of 5?', 'How many 8s are in 840?'] #list of questions
  g_correct =['23', '25', '105'] #list of correct answers 

  random.shuffle(g_questions)

  while len(g_questions) > 0: 
    if g_questions[0] == 'What is 12 + 11?':
      print (g_questions[0])
      answer = str(input("Enter your answer: "))
      if answer == g_correct[0]:
        print("Correct!")
        score +=1
        del g_questions[0]

      else:
        print("Incorrect")
        del g_questions[0]

    elif g_questions[0] == 'What is the square of 5?':
      print (g_questions[0])
      answer = str(input("Enter your answer: "))
      if answer == g_correct[1]:
        print("Correct!")
        score +=1
        del g_questions[0]
    
    
        

      else:
        print("Incorrect")
        del g_questions[0]

    elif g_questions[0] == 'How many 8s are in 840?':
      print(g_questions[0])
      answer = str(input('Enter your answer: '))
      if answer == g_correct[2]:
        print('Correct!')
        score += 1
        del g_questions[0]
      
      else:
        print('Incorrect')
        del g_questions[0]

    print("Your score is:", score)  

def help_section():
  #display help menu
  print()
  print(40 * "-")
  print("\n1. Multiple Choice")
  print("\n2. General Answer\n")
  print(40 * "-")
  #user chooses which part to display help for
  helpChoice = input("What are do you need help with? (1 or 2)")
  #short explanation for two types of quizzes are displayed
  if helpChoice == "1":
    print("The multiple choice section will give you a question and a choice of answers, just enter the number of the answer you think is right")
  elif helpChoice == "2":
    print ("The general answer will give you a question and you must type your own answer in ")
  else:
    print ("invalid choice, please enter a number 1, 2 or 3")
  
def main_menu(multiple_choice, general_answer, help_section):
  while True:
      print()
      print(40 * "-")
      print("     Maths Quiz     ")
      print("\n1. Multiple Choice")
      print("\n2. General Answer")
      print("\n3. Help")
      print("\n4. Quit\n")
      
      print(40 * "-")

  

  

      menu_choice = input("Choose an option (1, 2, 3 or 4): ")

      if menu_choice == "1":
        multiple_choice()
        break
        
    
      elif menu_choice == "2":
        general_answer()
        break
        
      elif menu_choice == "3":
        help_section()
        break

  
      elif menu_choice == "4":
        print ("Goodbye")
        break
  
      else:
        print ("invalid choice, please enter a number 1, 2, 3 or 4")

main_menu(multiple_choice, general_answer, help_section)


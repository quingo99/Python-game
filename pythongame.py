# Qui Ngo
# Feb 10, 2021
 
 # This is a game to demo functions in python 

 # Rock Paper Scissors
  # Rock beats Scissors
  # Scissors beat paper
  # Paper beats Rock

  # Pseudocode -->
  # User selection
  # Computer Selection -- get info from user
  # Evaluate the result 
  # Declare a winner
import random

possible_choices = ['Rock', 'Paper', 'Scissor']
while True: 
  user_selection = input('What is your selection? (Rock, Papers, Scissors): ')
  print('you choose:', user_selection)
  computer_selection = random.choice(possible_choices)

  #random.choices is multiple choice. 
  #computer_selection = "Rock"
  print('compute choose:', str(computer_selection))

  # Evaluate the resul
  if user_selection == computer_selection:
    print('It is a tie')
  elif user_selection == 'Rock':
        if (computer_selection =='Scissor'):
              print("Congratulation you're winner")
        else :
              print("Opp! You're lose")
  elif user_selection == "Scissor" :
        if (computer_selection =='Paper'):
              print("Congratulation you're winner")
        else :
              print("Opp! You're lose")
  elif user_selection == 'Paper':
        if (computer_selection =='Rock'):
              print("Congratulation you're winner")
        else :
              print("Opp! You're lose")
  play_again = input('Do you want to play again (y/n): ')
  if play_again == 'n':
        break
        #break out of loop

# This is outside of the loop
print ('Thanks for playing')




import random

stages = ['''
  
=========''', '''
   +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''']
#words to guess
word_to_guess = ["new", "style","play","job", "try", "game"]
#randomly chose a word
random_chosen_word =random.choice(word_to_guess)
print(random_chosen_word)
 #get a list to store the chosen word
display = []
word_length=len(random_chosen_word)
#creating a variable called lives to keep record of the number of lives
lives=6
#CHECK guessed letter
for _  in range(len(random_chosen_word)):
    display += "_"#replace underscore with letter the user guessed
game_over =False
#loop
while not game_over:
    # get a letter from user
    guessed_letter = input("Guess a letter: ")
    for position in  range(word_length):
        letter = random_chosen_word[position]
       # print(f"Current position{position}\n Current letter: {letter}\n guessed letter")
        if letter ==guessed_letter:
            display[position]=letter
    #check if guess is not in chosen word and replace it with a lost live
    if guessed_letter not in random_chosen_word:
        lives -=1
        print(stages[lives])
        if lives==0:
            game_over=True

            print("You lose")


            #print list replacing the blanks with the guessed_letter
    print(f"{' '.join(display)}")
    if "_" not in display:# check if blanks are not in the random_chosen_word
        game_over = True#flip game_over to true, so as to end the loop
        print("You win")



import random
#words to guess
word_to_guess = ["new", "style","play","job", "try", "game"]
#randomly chose a word
random_chosen_word =random.choice(word_to_guess)
print(random_chosen_word)
game_over =False
#loop


 #get a list to store the chosen word
display = []
word_length=len(random_chosen_word)
#CHECK guessed letter
for _  in range(len(random_chosen_word)):
    display += "_"#replace underscore with letter the user guessed


while not game_over:
    # get a letter from user
    guessed_letter = input("Guess a letter: ")
    for position in  range(word_length):
        letter = random_chosen_word[position]
       # print(f"Current position{position}\n Current letter: {letter}\n guessed letter")
        if letter ==guessed_letter:
            display[position]=letter
            #print list replacing the blanks with the guessed_letter
            print(display)
            if "_" not in display:
                game_over = True
                print("You win")



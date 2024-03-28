import random
import assets
print(f"{assets.logo}\n\n")
word_list = assets.word_list
chosen_word = random.choice(word_list)
game_over = False
lives = 6
print(chosen_word)

display_word_characters = []
for i in range (0, len(chosen_word)):
    display_word_characters.append("_")

while(not game_over):
    print(assets.stages[lives])
    print(f"\n Your Word: {' '.join(display_word_characters)}")
    user_guess = input("Guess a letter: ")
    initial_dash_count = display_word_characters.count("_")
    for index,letter in enumerate(chosen_word):
        if letter == user_guess.lower():
            display_word_characters[index] = letter       
        else:
           pass
    if(display_word_characters.count("_") == initial_dash_count):
        if user_guess in display_word_characters:
            print(f"You already guessed {user_guess}")
        else:
            print(f"You guessed {user_guess}, thats not in the word. You lose a life")
            lives += -1

    display_word = ' '.join(display_word_characters)
    print(display_word)
    if '_' not in display_word_characters:
        game_over = True
        print("YOU WON")
        print(f"\nThe word is {chosen_word}")
        
    elif lives <1:
         game_over = True
         print(assets.stages[lives])
         print("YOU LOST")
         print(f"\nThe word was {chosen_word}")

    else:
        pass
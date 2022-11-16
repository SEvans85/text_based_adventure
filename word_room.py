def word_room():
    letters = ['u', 'o', 'c', 't', 's', 't', 'a', 'e', 'l']
    attempts = 6
    word = 'castle'
    print(f"You appear to have bumped your head.. openeing your eyes slowly")
    print(f'You see a chest in the middle of the room, intrigued.. you walk over and look inside..')
    print(f'Inside there are 8 tiles, with blood carvings.. they appear to be letters')
    print('You hear a roar in the distance..')
    while attempts != 0:
        guess = str(input("Word Worgen: Guess the 6 letter word and you may pass: "))
        if len(guess) != 6:
            print("Enter a 6 letter word, dummy!")
            print(f"You have {attempts-1} tries left.")
            attempts -= 1
            if attempts == 0:
                #dead()
                print('you are dead')
        else:
            if guess == word:
                print("Word Worgen: wait.. what?! how did you do that?!")
                break
            else:
                attempts += 1
                print(f"You have {attempts} tries left.")
                for hidden_c, guess_c in zip(word, guess):
                    if guess_c in word and guess_c in hidden_c:
                        print(guess_c+ u' \u2713 ')
                    elif guess_c in word:
                        print(guess_c + ' + ')
                    else:
                        print(' X ')
            if attempts == 0:
                #dead():
                print('you are dead')

word_room()



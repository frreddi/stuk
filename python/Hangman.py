
try:
    oneMore = str('');
    while True:
        all = [];
        right = [];
        guess = str('!1984!');
        secret_word = str('!1984!');
        numberOfGuesses = int(-1984);
        tog = bool(False);
        
        while not secret_word.isalpha():
            secret_word = str.upper(input("\n\nWhat's the password, member: "));
            if not secret_word.isalpha():
                print('Only letters here XY/XX!');
        hiddenList = list('*' * len(secret_word));
        
        while numberOfGuesses <= 0:
            numberOfGuesses = abs(int(input('Now, how many guesses do you wanna give them? Natural numbers only only: ')));
            print();
            if numberOfGuesses <= 0:
                print('I guess you most have guesses to guess, or...?');
        
        print('\n'*42);
        print('\n'*13);
        
        
        print('Welcome. The secret word has', len(secret_word), 'letters, and you have', numberOfGuesses, 'guesses.\n');
        
        while oneMore == '':
            
            if tog == True:
                print();
                if numberOfGuesses == 1:
                    print('Last try!');
                else:
                    print('Tries left:', numberOfGuesses);
                print('Guessed:', ''.join(sorted(all)));
                print('Right guesses:', ''.join(sorted(right)));
            tog = True;
            print();
            print(''.join(hiddenList));
            
            if ''.join(hiddenList) == secret_word:
                print('\nCongratulations, you found the secret word! It was:', secret_word + ', GG :D');   #Win animation
                break;
            if numberOfGuesses == 0:
                print("\nYou are out of guesses. Op fail'd :/");   #Loss animation
                break;
            
            del guess;
            guess = str.upper(input('\nGuess a letter in the secret word: '));
            print('\n'*3);
            print('Guessed:', guess);
            if len(guess)!=1:
                print('Plz guess at one letter at a time...');
                continue;
            if not guess.isalpha():
                print('Only a letter here XY/XX!');
                continue;
            if guess in all:
                print('You already guessed this :3');
                continue;
            all.append(guess);
            
            if guess in secret_word:
                right.append(guess);
                print('You guessed a correct letter, GJ!');
                for x in range (len(secret_word)):
                    if secret_word[x] == guess:
                        del hiddenList[x];
                        hiddenList.insert(x, secret_word[x]);
            
            else:
                numberOfGuesses-=1;
                print('Sorry, wrong guess. Better luck next time.');   #Draw here
        
        oneMore = input('Press enter for a new game: ');
        if oneMore != '':
            break;

except:
    input('\nAn error occurred :o Press a key to exit. ');
    quit();

finally:
    print('Thank you for playing! :)');
    quit();

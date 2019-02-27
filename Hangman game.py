
try:
    oneMore = str('');
    while True:
        all = [];
        right = [];
        guess = str('!1984!');
        secret_word = str('!1984!');
        tog = bool(False);
        
        while not secret_word.isalpha():
            secret_word = str.upper(input("\n\nWhat's the password, member: "));
            if not secret_word.isalpha():
                print('Only letters here XY/XX!');
        hiddenList = list('*' * len(secret_word));
        
        numberOfGuesses = int(input('Now how many guesses do you wanna give them, integers only: '));
        
        print('\n'*42);
        print('\n'*13);
        
        
        print('The secret word has', len(secret_word), 'letters, and you have', numberOfGuesses, 'guesses.\n');
        
        while oneMore == '':
            
            if tog == True:
                if numberOfGuesses == 1:
                    print('Last try!');
                else:
                    print('Tries left:', numberOfGuesses);
                print('Guessed:', ''.join(sorted(all)));
                print('Right guesses:', ''.join(sorted(right)));
            tog = True;
            print(''.join(hiddenList));
            
            if ''.join(hiddenList) == secret_word:
                print('\nCongratulations, you found the secret word! It was:', secret_word + ', GG :D');   #Win animation
                break;
            if numberOfGuesses == 0:
                print("\nYou are out of guesses. Op fail'd");   #Loss animation
                break;
            
            del guess;
            guess = str.upper(input('\nGuess a letter in the secret word: '));
            print('\n');
            if not guess.isalpha():
                print('Only a letter here XY/XX!');
                continue;
            if len(guess)!=1:
                print('Plz guess at one letter at a time...');
                continue;
            if guess in all:
                print('You already guessed this.');
                continue;
            all.append(guess);
            
            if guess in secret_word:
                right.append(guess);
                print('You guessed a correct letter! GJ');
                for x in range (len(secret_word)):
                    if secret_word[x] == guess:
                        del hiddenList[x];
                        hiddenList.insert(x, secret_word[x]);
            
            else:
                numberOfGuesses-=1;
                print('Sorry, wrong guess. Better luck next time.');   #Draw here
        
        oneMore = input('Press enter for a new game.');
        if oneMore != '':
            break;

except:
    input('An error occurred. Press a key to exit.');
    quit();

finally:
    print('Thank you for playing! :)');
    quit();


secret_word=str.upper(input("\n\nWhat's the password, member: "))
        
numberOfGuesses=int(input("Now how many guesses do you wanna give them: "))

all=[]
right=[]
secret_wordList=list(secret_word)
guessList=[]
hiddenList=list("*" * len(secret_word))
guess=str("!1984!")


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


print("The secret word has", len(secret_word), "letters.\n")

while True:

    if guess in secret_word:
        guessList=list(guess)
        for x in range (0, len(secret_word)):
            if len(secret_word)>x and secret_word[x]==guessList[0]:
                del hiddenList[x]
                hiddenList.insert(x, secret_wordList[x])

    print(''.join(hiddenList))

    if ''.join(hiddenList)==secret_word:
        print("\nCongratulations, you found the secret word! It was: " + secret_word + ", GG :D\n")   #Win animation
        break

    if numberOfGuesses==0:
        print("\nYou are out of guesses. Op fail'd")   #Lose animation
        break

    del guess
    guess=str.upper(input("\nGuess a letter in the secret word: "))
    if len(guess)!=1:
        print("Plz guess at one letter at a time...\n")
        continue
    if guess in all:
        print("You already guessed this.\n")
        continue

    all.append(guess)
    print("Guesses:", ''.join(sorted(all)))
    if guess in secret_word:
        right.append(guess)
    print("Right guesses:", ''.join(sorted(right)))
    if guess in secret_word:
        print("You guessed a correct letter! GJ\n")
        continue
    else:
        numberOfGuesses-=1
        print("Wrong guess. You have:", numberOfGuesses, "tries left.\n")   #Draw here


input("Press a key to exit.")
quit()

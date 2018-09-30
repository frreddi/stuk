
hemmelig_ord=str.upper(input("\n\nWhat's the password, member: "))
        
antall_gjettninger=int(input("Now how many guesses do you wanna give them: "))

all=[]
right=[]
hemmelig_ordList=list(hemmelig_ord)
gjettList=[]
hiddenList=list("*" * len(hemmelig_ord))
gjett=str("!1984!")


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


print("The secret word has", len(hemmelig_ord), "letters.\n")

while True:

    if gjett in hemmelig_ord:
        gjettList=list(gjett)
        for x in range (0, len(hemmelig_ord)):
            if len(hemmelig_ord)>x and hemmelig_ordList[x]==gjettList[0]:
                del hiddenList[x]
                hiddenList.insert(x, hemmelig_ordList[x])

    print(''.join(hiddenList))

    if ''.join(hiddenList)==hemmelig_ord:
        print("\nCongratulations, you found the secret word! It was: " + hemmelig_ord + ", GG :D\n")   #vinn animasjon, slipp karakteren fri
        break

    if antall_gjettninger==0:
        print("\nYou are out of guesses. Op fail'd")   #tap animasjon, heng karakteren
        break

    del gjett
    gjett=str.upper(input("\nGuess a letter in the secret word: "))
    if len(gjett)!=1:
        print("Plz guess at one letter at a time...\n")
        continue
    if gjett in all:
        print("You already guessed this.\n")
        continue

    all.append(gjett)
    print("Guesses:", ''.join(sorted(all)))
    if gjett in hemmelig_ord:
        right.append(gjett)
    print("Right guesses:", ''.join(sorted(right)))
    if gjett in hemmelig_ord:
        print("You guessed a correct letter! GJ\n")
        continue
    else:
        antall_gjettninger-=1
        print("Wrong guess. You have:", antall_gjettninger, "tries left.\n")   #tegn her


input("Press a button to exit.")
quit()

import random
#variables needed
lst = ["dog", "cat", "peter"]

# Hello World

#Gets the random word
def get_word():
    a = random.randint(0,2)
    return lst[a]

def word_or_letter(): #asks the user if they want to guess the word or letter
    while True:       #then asks them for their guess
        p = str(input("Do you want to guess the word or letter"))
        if p == "word":
            l = str(input("Guess a word."))
            if l.isdigit() == True or len(l) < 2: #if its a digit or more than 1 letter
                print("Not a valid word, try again")
                continue
            else:
                return l
                break
                    

        if p == "letter":
            l = str(input("Guess a letter."))
            if l.isdigit() == True or len(l) > 1:
                print("Not a valid letter, try again")
                continue
            else:
                return l
                break

word = get_word() #assigns the actual word to variable word

lives_remaining = 7 #lives remaining
test = [] # sets empty list
for x in range(0,len(word)):
    test.append("_")
    #adds _ to however many letters are needed
    
while True:
    check = 0 #number to see if any of letters were right
    letters_in_a_row = 0 #checks how many times that letter appeared
    guess = word_or_letter() # assigns your guess to the variable guess
    if len(guess) > 1: #distingueshes the guess to a word to see if its more than 1 letter
        if guess == word: #checks if it matches
            print("Congrats you won")
            break
        else:
            print("Nope thats not it, try again")
            lives_remaining -=1 #decreases by 1 life
            print("You have %s guesses left" % lives_remaining)
            continue

    for x in range(0,len(word)):
        if word[x] == guess: #if that letter is the guess
            del test[x] #deletes that index with the underscore
            test.insert(x, guess) #adds that index back with the letter
            check += 1 #knows 1 of guesses is right, doesn't cost a life
            letters_in_a_row += 1 #how many letters they got

    if check == 0: #if its 0, means the letter wasn't right
        lives_remaining -=1
        print("Nope, that letter wasn't in the word\nYou have %s lives left" % lives_remaining)
        continue
        
            
    print (test)#prints the word to show what you got right or wrong
    
    if word == ''.join(test): #converts the list into a string, comparing it to the word
        print("Congrats, you got the word!")
        break
    
    print("You guessed %s correctly" % letters_in_a_row)
    #tells you how many you guessed right
    
    if lives_remaining == 0: #if you ran out of lives
        print("Out of guesses, the word was %s" % word)
        break


    

    
    
            

    
    





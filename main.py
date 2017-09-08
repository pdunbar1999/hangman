import random
lst = ["dog", "cat", "peter"]


#Gets the random word
def get_word():
    a = random.randint(0,2)
    return lst[a]

def word_or_letter():
    while True:
        p = str(input("Do you want to guess the word or letter"))
        if p == "word":
            l = str(input("Guess a word."))
            if l.isdigit() == True or len(l) < 2:
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

word = get_word()
print (word)


count = 7
test = []
for x in range(0,len(word)):
    test.append("_")
    
while True:
    p = 0
    letters_in_a_row = 0
    guess = word_or_letter()
    if len(guess) > 1:
        if guess == word:
            print("Congrats you won")
            break
        else:
            print("Nope thats not it, try again")
            count -=1
            print("You have %s guesses left" % count)
            continue

    for x in range(0,len(word)):
        if word[x] == guess:
            del test[x]
            test.insert(x, guess)
            p += 1 #knows 1 of guesses is right, doesn't cost a life
            letters_in_a_row += 1 #how many letters they got

    if p == 0:
        count -=1
        print("Nope, that letter wasn't in the word\nYou have %s lives left" % count)
        continue
        
            
    print (test)
    if word == ''.join(test):
        print("Congrats, you got the word!")
        break
    print("You guessed %s correctly" % letters_in_a_row)
    
    if count == 0:
        print("Out of guesses, the word was %s" % word)
        break

    if word == ''.join(test):
        print("Congrats, you got the word!")
        break

    

    
    
            

    
    





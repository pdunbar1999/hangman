global words
import random
lst = ["dog", "cat", "peter"]


#Gets the random word
def get():
    a = random.randint(0,2)
    return lst[a]

def guess():
    while True:
        l = str(input("Guess a letter."))
        if l.isdigit() == True or len(l) > 1:
            print("Not a valid letter, try again")
            continue
        else:
            return l
            break

word = get()
print (word)

while True:
    count = 0
    letter = guess()
    print (letter)

    for x in range(0,len(word)):
        if word[x] == letter:
            print("Theres one")
            count +=1
    print("You got %s" % count)
        

            

    
    





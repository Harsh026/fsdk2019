"""
Challenge 1

    We are going to make a "Hangman Letter" game 
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.

Algorithm

    # import external libraries
    # make a list of word

    # pick a random word

    # draw  spaces
    # take guess
    # draw guessed letters, spaces and strikes
    # print out win / lose

"""
import random 
  
wordlist="apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon"
wordlist1 = wordlist.split(' ')  
word = random.choice(wordlist)
turns =len(word)+2

for i in word:
    print("_",end=" ")
print("Guess letter one at a time :") 
guesses = ''
while (turns > 0):         
    failed = 0       
    guess = input("guess a character:") 
    guesses += guess                              
    for char in word:      
        if char in guesses:    
            print (char)    

        else:
            print ("_")     
            failed += 1    

    
    if failed == 0:        
        print("You won")  
        break              
    
    if guess not in word:  
        turns -= 1
        print ("Wrong")
        print("You have", + turns, "more guesses") 
    if turns == 0:      
        print("You Loose")
  
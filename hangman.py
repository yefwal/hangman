import wordbank
import random
import sys
import hanging

def start():
    start = input(r"""

    Select a genre:

    - Animals
    - Fruits
    - Countries
    - Professions
    - Colors 
    - Technology

    Genre:

    """)
    global randWord
    randWord = random.choice(wordbank.genres[start])
    if start in wordbank.genres:
        print(r"""

            _______
        |/      |
        |      
        |      
        |      
        |      
        |
       _|___

    """)
        
        length = len(randWord)
        print(randWord)
        print("_ " * length)
    
    guess(randWord)


def guess(word, count=0):
    global randWord
    length = len(randWord)
    hidden = "_ " * length

    while True:
        attempt = input("Type a letter! ")

        if len(attempt) == 1:
            break
        else:
            print("Please enter only one letter!")

    found = False
    
    for i in randWord:
        if i == attempt:
            found = True
            print("_ " * (length - 1)) 

    if not found:
        count += 1
        if count == 1:
            hanging.display_hangman("head")
        elif count == 2:
            hanging.display_hangman("body")
        elif count == 3:
            hanging.display_hangman("legs")
        elif count == 4:
            hanging.display_hangman("arms")
            
        print(f"Wrong Attempts: {count}")
        print(hidden)
        
    # Check for game over condition
    if count >= 4:
        print("Game over!")
        return  # Return to stop further recursive calls
    else:
        guess(word, count)  # Recursive call for next attempt

def game():
    start()

game()


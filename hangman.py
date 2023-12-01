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
    global empty
    empty = []
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
        while len(empty) < length:
            empty.append("_")
        print(randWord)
        print(" ".join(empty))
    guess(randWord)


def guess(word, count=0):
    global randWord
    global newWord
    length = len(randWord)

    while True:
        attempt = input("Type a letter! ")

        if len(attempt) == 1:
            break
        else:
            print("Please enter only one letter!")

    found = False
    
    for index, letter in enumerate(randWord):
        if letter == attempt:
            found = True
            empty[index] = attempt
            newWord = (" ".join(empty))
            print(newWord)
        if "_" not in newWord:
            print("You Win!")
            return

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
        print(newWord)
        
    # Check for game over condition
    if count >= 4:
        print("Game over!")
        return 
    else:
        guess(word, count) 

def game():
    start()

game()


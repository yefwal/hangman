#step1

step1 = [

r"""
        _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
    """
]

#step2

step2 = [

r"""
        _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___
    """
]

#step3 

step3 = [

r"""
        _______
     |/      |
     |      (_)
     |       |
     |       |
     |      / \
     |
    _|___
    """
]

#step4

step4 = [

r"""
        _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___
    """
]

stages = {
    "head": step1,
    "body": step2,
    "legs": step3,
    "arms": step4,
}

def display_hangman(stage):
    for line in stages[stage]:
        print(line)
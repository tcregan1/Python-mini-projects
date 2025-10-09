
from random_word import RandomWords
r = RandomWords()

stage = 0


def start_game():
    word = r.get_random_word()
    current_layout = list(word)
    i = 0
    for x in current_layout:
        current_layout[i]= "_"
        i += 1
    return current_layout, word

def letter_guess(word: str, current_layout: list):
    global stage
    i = 0
    found = False
    letter = input("Enter a letter bozo: ")
    for x in word:
        if x == letter:
            current_layout[i] = letter
            found = True
        i += 1
    if found == False:
        stage += 1
        execution_stage(stage)
        print_list(current_layout)
    elif found == True:
        print_list(current_layout)
 

def word_guess(word:str):
    global stage
    guess = input("Take a guess bozo: ")
    if guess == word:
        print("Congrats you fucking nerd, you win !!!") 
        quit()
    else:
        stage+= 1
        print("Your a godamn retard !!!")
        execution_stage(stage)

def print_list(cl:list):
    return print(*cl, sep=' ')


def stage_zeo():
    return
def stage_one():
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''']
    return print_list(HANGMANPICS)

def stage_two():
    HANGMANPICS = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''']
    return print_list(HANGMANPICS)

def stage_three():
    HANGMANPICS = ['''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''']
    return print_list(HANGMANPICS)

def stage_four():
    HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''']
    return print_list(HANGMANPICS)

def stage_five():
    HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''']
    return print_list(HANGMANPICS)

def stage_six():
    HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''']
    return print_list(HANGMANPICS)
    
def stage_seven():
    HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
    return print_list(HANGMANPICS)

def execution_stage(stage: int):
    switcher = {
        0:stage_zeo,
        1:stage_one,
        2:stage_two,
        3:stage_three,
        4:stage_four,
        5:stage_five,
        6:stage_six,
        7:stage_seven
    }
    result = switcher.get(stage, lambda: "unknown")()
    return result


cl, word = start_game()

while(stage != 7):
    choice = input("Would you like to guess a letter(l) or a word(w): ")
    if(choice == "w"):
        word_guess(word)
    if(choice == "l"):
        letter_guess(word, cl)


print("You suck bro, word was: ", word)
def main():
    secret_word = get_secret_word()
    correct_guesses = ""
    wrong_guesses = ""

    while (not word_is_solved(secret_word, correct_guesses) and
            not player_is_dead(wrong_guesses)):
        display_platform(wrong_guesses)
        display_letters(secret_word, correct_guesses)
        guess = get_guess()

        # HANDLE GUESS
        # if guess is in the word, the add it to the correct guesses
        # otherwise, add it to the incorrect guesses
        
        if guess in secret_word:
            correct_guesses += guess
        else:
            wrong_guesses += guess


    if word_solved(secret_word, correct_guesses):
        show_win_screen()
    else:
        show_lose_screen()


def get_secret_word():
    """Will return a single word from a list of words.

    Returns:
        Single word from a list
    """
    pass


def word_is_solved(word, guesses):
    """Will check to see if a word has been completely solved.

    Args:
        word (str): The secret word
        guesses (str): The string containing all correct guesses

    Returns:
        bool: True if word is solved, False if word is not.
    """
    total = 0  # number of guessed characters in word

    for guess in guesses:
        # Number of guesses[i] in word
        num = word.count(guess)
        if num > 0:
            total += num
    if total == len(word):
        return True
    else:
        return False



def player_is_dead(wrong_guesses):
    """Determines if the player is dead (too many guesses).

    Args:
        bad_guesses (str): A string containing all of the wrong guesses

    Returns
        bool: True if dead, False otherwise
    """
    player_is_dead = False

    if len(wrong_guesses) >= 6:
        player_is_dead = True

    return player_is_dead


def display_platform(wrong_guesses):
    """Displays (prints) hanging platform based on how many incorrect guesses.
    
    Args:	
    	wrong_guesses (str): A string containing all wrong guesses.
    """
    zero_incorrect = """
    _________
    |        |
             |
             |
             |
             |
             |
             |
    _________|_______
    """

    one_incorrect = """
    _________
    |        |
    O        |
             |
             |
             |
             |
             |
    _________|_______
    """

    two_incorrect = """
    _________
    |        |
    O        |
    |        |
    |        |
             |
             |
             |
    _________|_______
    """

    three_incorrect = """
    _________
    |        |
    O        |
  --|        |
    |        |
             |
             |
             |
    _________|_______
    """

    four_incorrect = """
    _________
    |        |
    O        |
  --|--      |
    |        |
             |
             |
             |
    _________|_______
    """

    five_incorrect = """
    _________
    |        |
    O        |
  --|--      |
    |        |
   /         |
             |
             |
    _________|_______
    """

    six_incorrect = """
    _________
    |        |
    O        |
  --|--      |
    |        |
   / \       |
             |
             |
    _________|_______
    """

    if num_wrong_attempts == 0:
        print(zero_incorrect)
    elif num_wrong_attempts == 1:
        print(one_incorrect) 
    elif num_wrong_attempts == 2: 
        print(two_incorrect) 
    elif num_wrong_attempts == 3:  
        print(three_incorrect)
    elif num_wrong_attempts == 4: 
        print(four_incorrect)
    elif num_wrong_attempts == 5:  
        print(five_incorrect) 
    elif num_wrong_attempts == 6:  
        print(six_incorrect)


def display_letters(word, guesses):
    """Displays (prints) the letter-board,
    underscores (_) for letters not yet guessed.

    Args:
        word (str): The secret word
        guesses (str): A string of correct guesses
    """
    pass


def get_guess():
    """Will take the user's guess. Ensures the input is valid.

    """
    letter = input("Please input a letter to check").lower()
    if len(letter) != 1:
        print("Please input a single letter")
        get_guess()
    elif letter not in "abcdefghijklmnopqrstuvxyz":
        print ("Only input letters")
        get_guess()
    else:
        return letter

    
def show_win_screen():
    """Will display ASCII art for a win screen"""
    print ("""
                                                   /$$           /$$
                                                  |__/          | $$
 /$$   /$$  /$$$$$$  /$$   /$$       /$$  /$$  /$$ /$$ /$$$$$$$ | $$
| $$  | $$ /$$__  $$| $$  | $$      | $$ | $$ | $$| $$| $$__  $$| $$
| $$  | $$| $$  \ $$| $$  | $$      | $$ | $$ | $$| $$| $$  \ $$|__/
| $$  | $$| $$  | $$| $$  | $$      | $$ | $$ | $$| $$| $$  | $$    
|  $$$$$$$|  $$$$$$/|  $$$$$$/      |  $$$$$/$$$$/| $$| $$  | $$ /$$
 \____  $$ \______/  \______/        \_____/\___/ |__/|__/  |__/|__/
 /$$  | $$                                                          
|  $$$$$$/                                                          
 \______/                                                           
""")


def show_lose_screen():
    """Will display ASCII art for a lose screen"""
    print("""
   
 _  _  __   _  _    __     __   ____  ____    _  _  
( \/ )/  \ / )( \  (  )   /  \ / ___)(  __)  (_)/ ) 
 )  /(  O )) \/ (  / (_/\(  O )\___ \ ) _)    _( (  
(__/  \__/ \____/  \____/ \__/ (____/(____)  (_)\_) 
""")


if __name__ == "__main__":
    main()

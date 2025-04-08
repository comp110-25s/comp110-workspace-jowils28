"""Lets Play Wordle"""

__author__: str = "730774862"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    while turns < 7:  # tells how many turns the player starts with
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(player_guess=guess, secret_word=secret))
        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            break
        if guess != secret:
            turns += 1
        if turns == 7:  # keeps count of turns so there is no endless loop
            print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """checks to see is the given word is the right length"""
    guess: str = input(f"Enter a {secret_word_len} character word:")
    while len(guess) != secret_word_len:
        guess = input(
            f"That wasn't {secret_word_len} chars! Try again:"
        )  # uses the length of the string so that code does not only work for 5 letter words
    return guess


def contains_char(secret_word: str, search_character: str) -> bool:
    """checks to see if target character can be found in given string"""
    assert len(search_character) == 1, f"len('{search_character}') is not 1"
    index: int = 0
    while index < len(secret_word):
        if search_character == secret_word[index]:
            # tells if given letter is found in the secret word
            return True
        index += (
            1  # progresses toward False while statement so there is no infinite loop
        )
    return False
    # for when te letter is not found in the secret word


def emojified(player_guess: str, secret_word: str) -> str:
    """Tells if the given letter is in the secret word using emojis"""
    assert len(player_guess) == len(secret_word), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    empty: str = ""
    index1: int = 0
    index2: int = 0
    contains: str = ""
    while index1 < len(secret_word):
        if contains_char(secret_word, player_guess[index2]) is True:
            contains += "True"  # tells if the given letter is in the secret word
        else:
            contains += "False"  # tells if the given letter is not in the secret word
        if secret_word[index2] == player_guess[index2] and contains == "True":
            empty += GREEN_BOX  # if the given letter is in the secret word and is in the right index
        if player_guess[index2] != secret_word[index1] and contains == "True":
            empty += YELLOW_BOX  # if the given letter is in the secret word but the wrong index
        if contains == "False":
            empty += WHITE_BOX  # if the given letter is not in the secret word at all
        index1 += 1
        index2 += 1
        contains = ""

    return empty


if __name__ == "__main__":
    main(secret="codes")

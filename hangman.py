import random


def hangman():
    words_list = [
        "python",
        "java",
        "kotlin",
        "javascript",
        "ruby",
        "php",
        "csharp",
        "swift",
        "scala",
        "go",
    ]
    word = random.choice(words_list)
    lives = 5
    letters_in_word = set(word)
    correct_guesses = set()
    wrong_guesses = set()
    while len(letters_in_word) > 0 and lives > 0:
        word_list = [letter if letter in correct_guesses else "_" for letter in word]
        print(" ".join(word_list))
        player_guess = input("Guess a letter: ")
        if player_guess in correct_guesses or player_guess in wrong_guesses:
            print("You already guessed that letter")
        elif player_guess in letters_in_word:
            correct_guesses.add(player_guess)
            letters_in_word.remove(player_guess)
        elif player_guess not in word:
            wrong_guesses.add(player_guess)
            lives -= 1
            print(f"Wrong guess! You have {lives} lives left")
    if lives == 0:
        print(f"Game over! The word was {word}")
    else:
        print(f"Congratulations! You guessed the word")


hangman()

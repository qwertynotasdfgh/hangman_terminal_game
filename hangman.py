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
    guessed_letters = set()


hangman()

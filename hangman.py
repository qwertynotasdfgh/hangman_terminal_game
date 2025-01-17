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
    correct_letters = set()
    wrong_leteers = set()
    while len(letters_in_word) > 0 and lives > 0:
        word_list = [letter if letter in correct_letters else "_" for letter in word]
        print(" ".join(word_list))
        lives -= 1


hangman()

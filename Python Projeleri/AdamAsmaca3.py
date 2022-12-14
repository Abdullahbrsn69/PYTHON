# Bu bir adam asmaca oyundur. Bu oyunda bir kelimeyi tahmin etmeye çalışacaksınız. Eğer kelimeyi doğru athmin ederseniz, kelimenin tamamını yazın veya harf harf yazın
# Mesela kelime "python" ise, "python" veya "p", "y", "t", "h", "o", "n" şeklinde yazabilirsiniz. Her yanlış tahminde bir canınız azalır.
#  Eğer canınız bitene kadar kelimeyi tahmin edemezseniz, oyunu kaybedersiniz. Eğer kelimeyi tahmin ederseniz, oyunu kazanırsınız.

import random

words = ["python", "java", "kotlin", "javascript", "assembly", "C", "Go", "Rust", "Dotnet"]

print(" ------------------- H A N G M A N ------------------- ")

while True:
    print("1. Play Hangman")
    print("2. Exit")

    choice = input("Please select an option: ")

    if choice == "1":
        
        word = random.choice(words)

        guessed = set()

        lives = 6

        while lives > 0:
            print() 
            for letter in word:
                if letter in guessed:
                    print(letter, end="")
                else:
                    print("-", end="")
            print()

            guess = input("Input a letter: ")

            if len(guess) != 1:
                print("You should input a single letter")
            elif guess not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a lowercase English letter")
            elif guess in guessed:
                print("You've already guessed this letter")
            elif guess not in word:
                print("That letter doesn't appear in the word")
                lives -= 1
            else:
                guessed.add(guess)

            if not set(word) - guessed:
                print("You guessed the word!")
                print("You survived!")
                break
        else:
            print("You lost!")

    elif choice == "2":
        break

    
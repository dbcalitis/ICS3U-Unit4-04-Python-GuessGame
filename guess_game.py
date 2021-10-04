#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program is the number guessing game

import random


def main():
    # This function is the number guessing game
    answer = random.randint(0, 9)

    while True:
        # input
        guess_number = input("Enter a number as your guess (0-9): ")

        try:
            guess_number = int(guess_number)

            # process & output
            if guess_number == answer:
                print("You guessed correctly!")
                break
            elif guess_number > answer:
                print("You guessed too high!")
            else:
                print("You guessed too low!")
        except Exception:
            print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()

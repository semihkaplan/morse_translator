# Created by Semih Kaplan
# Copyright (c) 2020 - All Rights Reserved.

# Only works on Windows.

import time
import winsound

alphabet = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"
}

morse = ""
text = ""


def get_input():
    global morse, text
    while True:
        error = False
        text = input("Text to Morse: ").upper()
        for letter in text:
            if letter in alphabet:
                morse = morse + alphabet[letter] + " "

            else:
                error = True
                break

        if error:
            print("\nYou entered an invalid character!\n")
            continue

        else:
            break


def beep():
    for i in morse:
        if i == '.':
            winsound.Beep(750, 100)

        elif i == '-':
            winsound.Beep(750, 300)

        else:
            time.sleep(0.2)

        time.sleep(0.1)


get_input()
print("\n{}\n\n{}".format(text, morse))
beep()

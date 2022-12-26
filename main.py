"""Kirby Sign Generator - By: Gregory G.

The program will take in a user's inputed text and then output an ASCII art of Kirby holding up
that sign.

I do not own the rights to the Kirby franchise. The Kirby franchise is a property of Nintendo Co., Ltd

Program Steps:

1. Takes User Input
2. Create ASCII Art
    a) Convert text into ASCII art
    b) Create border around text
    c) Place Kirby in the centre of the text
3. Display ASCII Art
"""
from asciis import ascii_dict


def str_to_ascii(characters: str) -> list[list[list[str]]]:
    """
    Takes a string of letters of the alphabet in lowercase and returns the
    ASCII version of each of its characters from asciis.py in the form of
    a string table

    Preconditions:
    - all([97 <= ord(character) <= 122 for character in characters])
    """
    ascii_characters = []
    for char in characters:
        ascii_characters.append(ascii_dict[char])

    return ascii_characters


# Intro Messages
print('Kirby Drawing Generator v.01 - By: Gregory Gismondi')
print('Currently the generator only supports the 26 characters of the alphabet in lowercase\n')

# Taking User Input
message = input('Please input your message:')

# Converting to ASCII
ascii_message = str_to_ascii(message)

for letter in ascii_message:
    for row in letter:
        print(row)

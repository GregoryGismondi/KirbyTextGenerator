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
from asciis import ascii_dict, kirby


def str_to_ascii(characters: str) -> list[list[str]]:
    """
    Takes a string of letters of the alphabet in lowercase and returns the
    ASCII version of each of its characters from asciis.py. Returns a list
    of each ASCII characters value

    Preconditions:
    - all([97 <= ord(character) <= 122 for character in characters])
    """
    ascii_characters = []
    for char in characters:
        ascii_characters.append(ascii_dict[char])

    return ascii_characters


def ascii_creater(ascii_characters: list[list[str]]) -> list[str]:
    """
    Combines the ASCII artworks of the given strings into one ASCII artwork, with each row being an
    element in a list
    """
    main_ascii = []

    # Height of Sign = Tallest character + 2 (for spacing purposes)
    sign_height = -1 + max({len(ascii_character) for ascii_character in ascii_characters}) + 2

    # Width of Sign = Number of Spaces (# of characters - 1) + width of all characters
    sign_width = len(ascii_characters) - 1 + sum([len(ascii_character[0]) for ascii_character in ascii_characters])

    # Case 1: Sign Width < 32 (Must center text)
    if sign_width < 30:
        main_ascii.append('_' * 36)
        main_ascii.append('|' + ' ' * 34 + '|')

        for i in range(sign_height - 1, -1, -1):
            for ascii_character in ascii_characters:
                if i >= len(ascii_character):
                    main_ascii.insert(2, '| ' + ' ' * 32 + ' |')
                else:
                    main_ascii.insert(2, '| ' + ascii_character[i].center(32) + ' |')

        main_ascii.append('|' + kirby[0] + '|')
        for i in range(1, len(kirby)):
            main_ascii.append(' ' + kirby[i] + ' ')

    # Case 2: Sign Width >= (Must extend Kirby ASCII)

    return main_ascii


# Intro Messages
print('Kirby Drawing Generator v.01 - By: Gregory Gismondi')
print('Currently the generator only supports the 26 characters of the alphabet in lowercase\n')

# Taking User Input
message = input('Please input your message:')

# Converting to ASCII
ascii_message = str_to_ascii(message)

final_message = ascii_creater(ascii_message)

for row in final_message:
    print(row)

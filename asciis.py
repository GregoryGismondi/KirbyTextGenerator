"""Contains the ASCII artwork for the Kirby Sign Generator program

All ASCII artwork generated has been created either through the Figlet program
or my own personal creation

Key Notes on ASCIIs:

1. All rows of the ASCII lists MUST have the same length
2. ASCII characters must be added to the ascii_dict dictionary to be used
"""

# Kirby
kirby = ["_____-¯¯¯-______________-¯¯¯-_____",
         "    /     | __________ |     \    ",
         "   |  _-- ¯¯          ¯¯ --_  |   ",
         "  _└¯      .     v    .      ¯┘_  ",
         "_¯                              ¯_"]

# Letters
a_lower_block = ["  ###### ##",
                 " ##########",
                 "###     ###",
                 "##       ##",
                 "###     ###",
                 " ##########",
                 "  ###### ##"]

# Main List
ascii_dict = {'a': a_lower_block}

"""Contains the ASCII artwork for the Kirby Sign Generator program

All ASCII artwork generated has been created either through the Figlet program
or my own personal creation

Notes on ASCIIs:

1. All rows of the ASCII lists MUST have the same length or be blank (for spacing purposes)
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
                 "  ###### ##",
                 "", "", "", "", ""]

b_lower_block = ["##         ",
                 "##         ",
                 "##         ",
                 "##         ",
                 "##         ",
                 "## ######  ",
                 "########## ",
                 "###     ###",
                 "##       ##",
                 "###     ###",
                 "########## ",
                 "## ######  ",
                 "", "", "", "", ""]

c_lower_block = ["  ######## ",
                 " ##########",
                 "###      ##",
                 "##         ",
                 "###      ##",
                 " ######### ",
                 "  #######  ",
                 "", "", "", "", ""]

d_lower_block = ["         ##",
                 "         ##",
                 "         ##",
                 "         ##",
                 "         ##",
                 "  ###### ##",
                 " ##########",
                 "###     ###",
                 "##       ##",
                 "###     ###",
                 " ##########",
                 "  ###### ##",
                 "", "", "", "", ""]

e_lower_block = ["  #######  ",
                 " ######### ",
                 "###     ###",
                 "########## ",
                 "###        ",
                 " ######### ",
                 "  #######  ",
                 "", "", "", "", ""]

f_lower_block = ["    #####  ",
                 "  #########",
                 "  ###   ###",
                 "  ##       ",
                 "  ##       ",
                 "#######    ",
                 "######     ",
                 "  ##       ",
                 "  ##       ",
                 "  ##       ",
                 "  ##       ",
                 "  ##       ",
                 "", "", "", "", ""]

g_lower_block = ["  ###### ##",
                 " ##########",
                 "###     ###",
                 "##       ##",
                 "###     ###",
                 " ##########",
                 "  ###### ##",
                 "         ##",
                 "##       ##",
                 "###     ###",
                 " ######### ",
                 "   #####   "]

h_lower_block = ["##         ",
                 "##         ",
                 "##         ",
                 "##         ",
                 "##         ",
                 "## ######  ",
                 "########## ",
                 "###     ###",
                 "##       ##",
                 "##       ##",
                 "##       ##",
                 "##       ##",
                 "", "", "", "", ""]

i_lower_block = [" ## ",
                 "####",
                 "####",
                 " ## ",
                 "    ",
                 " ## ",
                 " ## ",
                 " ## ",
                 " ## ",
                 " ## ",
                 " ## ",
                 " ## ",
                 "", "", "", "", ""]

# Symbols
exclamation_mark_block = [" ######",
                          " ######",
                          " ######",
                          "  #### ",
                          "  #### ",
                          "   ##  ",
                          "   ##  ",
                          "       ",
                          "  #### ",
                          " ######",
                          " ######",
                          "  #### ",

                          "", "", "", "", ""]

# Special Characters
space_block = ["      "]

# Main List
ascii_dict = {' ': space_block, 'a': a_lower_block, 'b': b_lower_block, 'c': c_lower_block, 'd': d_lower_block,
              'e': e_lower_block, 'f': f_lower_block, 'g': g_lower_block, 'h': h_lower_block, 'i': i_lower_block,
              '!': exclamation_mark_block}

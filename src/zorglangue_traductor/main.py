# zorglangue-traductor
# by Raphaël DENNI

# Imports functions from shift.py and lower_upper.py
from src.zorglangue_traductor.utils.shift import shift
from src.zorglangue_traductor.utils.lower_upper import lower_upper


# Function that translates a string into Zorglangue
# Fun fact: Zorglonde is the name of the waves that transform people into Zorglhommes who speak Zorglangue
def zorglonde(string):
    string = string.split(" ")  # Split the string with spaces as separators to be able to reverse each word separately
    zorg_string = []

    punctuation_list = [",", ";", ":", ".", "?", "!"]

    # The next lines reverse each word of the string individually because they need to stay in the same order
    for i in range(0, len(string), 1):
        temp_list = list(string[i])

        if len(temp_list) > 1:  # The next lines are not executed if the word is only one letter long to avoid errors
            temp_list.reverse()

            # The next lines shift common ponctuations characters to the right after reversing a word,
            # because the function reverse() reverses these characters in a string
            # while they must remain at the same place.
            # This is necessary to correspond to the punctuation of the Zorglangue language (see shift.py)
            for j in punctuation_list:
                shift(temp_list, j)

            # The following case is specific to the apostrophe character
            # because it is the only character that is shifted to the left with another character
            # (e.g. with this, "l'appareil" becomes "l'lierappa" and not "lierappa'l")
            shift(temp_list, "'", 0, True)

            # The next line makes the letters lowercase and if needed capitalizes the first letter of the new string,
            # because the function reverse() places the first letter, which is commonly capitalized,
            # at the end of the word/string.
            # This is necessary to correspond to the letter capitalization of the Zorglangue language (see lower_upper.py)
            lower_upper(temp_list)

        zorg_string.extend(temp_list)
        zorg_string.append(" ")

    return "".join(zorg_string)


"""
    MIT License

    Copyright (c) 2023 Raphaël Denni
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""

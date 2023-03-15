# zorglangue-traductor
# by Raphaël DENNI

# Function that shifts a punctuation character to the right in a list
def shift(temp_list, value, position=190000, mate=False):  # The position argument is set to a high value to avoid errors
    if value in temp_list:
        j = temp_list.index(value)
        letter = temp_list[j + 1]

        temp_list.remove(value)
        temp_list.insert(position, value)

        # The following case is specific to the apostrophe character
        # because it is the only character that is shifted to the left with another character
        # (e.g. with this, "l'appareil" becomes "l'lierappa" and not "lierappa'l")
        if mate:
            temp_list.remove(letter)
            temp_list.insert(position, letter)


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

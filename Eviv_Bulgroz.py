# Programme de Zorglangue
# Par Raphaël DENNI

# Fonctions
def shift(value, position=190000, mate=False):
    global ch_temp
    if value in ch_temp:
        j = ch_temp.index(value)
        letter = ch_temp[j+1]

        ch_temp.remove(value)
        ch_temp.insert(position, value)

        if mate:
            ch_temp.remove(letter)
            ch_temp.insert(position, letter)


def maj():
    global ch_temp
    upper = 0
    for j in ch_temp:
        if j.isupper():
            upper += 1
               
    if upper == 1:
        ch_temp = (((str(ch_temp[0])).upper()) + (("".join(ch_temp[1:])).lower())).split(" ")


# Code principal
print("--- Programme de Zorglangue ---\n--- Par Raphaël DENNI ---")

while True:
    ch = input("\nEntrer votre chaîne de caractère : ").split(" ")
    ch1 = []

    for i in range(0, len(ch), 1):
        ch_temp = list(ch[i])

        ch_temp.reverse()

        shift(",")
        # shift(";")
        # shift(":")
        shift(".")
        # shift("?")
        # shift("!")
        shift("'", 0, True)

        maj()

        ch1.extend(ch_temp)
        ch1.append(" ")

    print("\nEviv Bulgroz :", "".join(ch1))

    input("\nAppuyez sur entrer pour une autre phrase ou cliquez sur la croix pour fermer")

"""
MIT License

Copyright (c) 2022 Raphaël Denni

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


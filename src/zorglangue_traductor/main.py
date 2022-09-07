# zorglangue-traductor
# by Raphaël DENNI

# Functions
def zorglonde(string):
    ch = string.split(" ")
    ch1 = []

    for i in range(0, len(ch), 1):
        ch_temp = list(ch[i])

        ch_temp.reverse()

        shift(ch_temp, ",")
        # shift(ch_temp,";")
        # shift(ch_temp,":")
        shift(ch_temp, ".")
        # shift(ch_temp,"?")
        # shift(ch_temp,"!")
        shift(ch_temp, "'", 0, True)

        maj(ch_temp)

        ch1.extend(ch_temp)
        ch1.append(" ")

    return "".join(ch1)


def shift(ch_temp, value, position=190000, mate=False):
    if value in ch_temp:
        j = ch_temp.index(value)
        letter = ch_temp[j + 1]

        ch_temp.remove(value)
        ch_temp.insert(position, value)

        if mate:
            ch_temp.remove(letter)
            ch_temp.insert(position, letter)


def maj(ch_temp):
    upper = 0
    for j in ch_temp:
        if j.isupper():
            upper += 1

    if upper == 1:
        ch_temp = (((str(ch_temp[0])).upper()) + (("".join(ch_temp[1:])).lower())).split(" ")


"""
   Copyright 2022 Raphaël Denni

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

# Zorglangue Traductor
A Python module that allows you to traduce the fake language Zorglangue from the Spirou comic strips. Works from a Latin language (originally French) to Zorglangue and vice versa. Eviv Bulgroz !

## Installation
```
py -m pip install zorglangue-traductor
```

## How to use it
Simply import the module into your Python 3 program, and you will be able to use the function `zorglonde` to traduce your string. The function takes a string as parameter and returns a string.
```
# Zorglangue Program
# by Raphaël DENNI

# Import
import zorglangue_traductor as zt

# Code
print("--- Zorglangue program ---\n--- by Raphaël DENNI ---")

while True:
    string = input("\nEnter your string : ")

    zorg_string = zt.zorglonde(string)

    print(f"\nEviv Bulgroz : {zorg_string})

    input("\nPress enter for an another phrase or shutdown the program.")
```

## Results example
![](https://i.imgur.com/JL9mOQN.png)
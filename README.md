# Zorglangue Traductor
A Python module that allows you to traduce the best language, Zorglangue. Works from a Latin language (originally French) to Zorglangue and vice versa. Eviv Bulgroz !

## Installation
```
py -m pip install zorglangue-traductor
```

## How to use it
Simply import the module into your Python 3 program, and be under Zorglub domination !
```
# Zorglangue Program
# by Raphaël DENNI

# Import
from zorglangue_traductor.main import zorglonde

# Code
print("--- Zorglangue program ---\n--- by Raphaël DENNI ---")

while True:
    string = input("\nEnter your string : ")

    zorg_traduction = zorglonde(string)

    print(f"\nEviv Bulgroz : {zorg_traduction})

    input("\nPress enter for an another phrase or shutdown the program.")
```

## Results example
![](https://i.imgur.com/JL9mOQN.png)
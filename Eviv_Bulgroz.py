# Programme de Zorglangue
# Par Raphaël DENNI

# Import
from main import zorglangue

# Code principal
print("--- Programme de Zorglangue ---\n--- Par Raphaël DENNI ---")

while True:
    string = input("\nEntrer votre chaîne de caractère : ")

    zorg_traduction = zorglangue(string)

    print("\nEviv Bulgroz :", "".join(zorg_traduction))

    input("\nAppuyez sur entrer pour une autre phrase ou cliquez sur la croix pour fermer")

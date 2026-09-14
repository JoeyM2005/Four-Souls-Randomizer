import random

chars = ["Isaac", "Maggy", "Cain", "Judas", "Blue Baby", "Eve",
"Samson", "Lazarus", "Lilith", "The Forgotten", "Eden", "Azazel",
"Tainted Forgotten", "Jacob & Esau", "Tainted Apollyon",
"Tainted Blue baby", "Flash Isaac", "Tainted Keeper", "Bethany",
"Tainted Eve", "Tainted Cain", "Tainted Bethany", "The Lost",
"Tainted Lazarus", "Tainted Lilith", "Tainted Eden", "Tainted Judas",
"Tainted Lost", "Tainted Isaac", "Tainted Jacob", "Tainted Maggy",
"Tainted Azazel", "Tainted Samson"]

players = int(input("How many players? "))

for i in range(players):
    playChar = random.choice(chars)
    print(playChar)
    chars.remove(playChar)

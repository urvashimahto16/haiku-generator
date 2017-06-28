from random import *

three_syllable = [ "Eat tissues", "Girls who code", "Spicy Memes", "Tupperware", "Back Table", "Falling Snow"]
five_syllable = ["That's plagiarism", "Blond hair till year five", "Bad snakes wear pythongs", "Free lunch everyday", "Don't be an onion", "Jacob Sartorius"]

first = randint(0, len(three_syllable) - 1)
print(three_syllable[first])
second = randint(0, len(five_syllable) - 1)
print(five_syllable[second])
third = randint(0, len(three_syllable) - 1)
print(three_syllable[third])

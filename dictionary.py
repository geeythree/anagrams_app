import pandas as pd
words = []
with open("words.csv") as file:
    file = file.readlines()
for word in file:
    words.append(word.replace("\n", ""))
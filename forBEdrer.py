import pandas as pd
import random as rd

INPUT_FILE_NAME = "input.csv"
OUTPUT_FILE_NAME = "output.csv"
WORD_LIST_FILE_NAME = "wordlist.txt"

wordlist = []

with open(WORD_LIST_FILE_NAME, "r") as file:
    data = pd.read_csv(file, sep="=")

for line in data:
    replacement_words = line[0].split(";")

for line in text:
    print(line)

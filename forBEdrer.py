import random as rd

INPUT_FILE_NAME = "input.csv"
OUTPUT_FILE_NAME = "output.csv"
WORD_LIST_FILE_NAME = "wordlist.txt"

wordlist = []


with open(WORD_LIST_FILE_NAME, "r") as file:
    data = file.read().splitlines()
    list = []
    for line in data:
        list.append(line.split('='))

for line in list:
    print(line)
    replacement_words = line[0].split(";")
    replaced_words = line[1].split(";")

    wordlist.append([{"replacement_words": replacement_words,"replaced_words": replaced_words}])

print(wordlist)

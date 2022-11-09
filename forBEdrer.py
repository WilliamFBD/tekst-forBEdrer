import random as rd

INPUT_FILE_NAME = "input.csv"
OUTPUT_FILE_NAME = "output.csv"
WORD_LIST_FILE_NAME = "wordlist.txt"

wordlist = []


with open(WORD_LIST_FILE_NAME, "r") as file:
    data = file.read().splitlines()
    split_data = []
    for line in data:
        split_data.append(line.split('='))

for line in split_data:
    replacement_words = line[0].split(";")
    replaced_words = line[1].split(";")

    wordlist.append([{"replacement_words": replacement_words, "replaced_words": replaced_words}])

with open(INPUT_FILE_NAME, "r") as file:
    data = file.read().splitlines()
    for line in data:
        for word in line.split(" "):
            for item in wordlist:
                if word in item[0]["replaced_words"]:
                    line = line.replace(word, rd.choice(item[0]["replacement_words"]))

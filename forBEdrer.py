import random as rd
import os

INPUT_FILE_NAME = "input.csv"
OUTPUT_FILE_NAME = "output.csv"
WORD_LIST_FILE_NAME = "wordlist.txt"

wordlist = []
error_text = ""
run = True

if not os.path.isfile(INPUT_FILE_NAME):
    raise FileExistsError("Input file does not exist")
    run = False
    error_text.append("Input file does not exist")
if not os.path.isfile(WORD_LIST_FILE_NAME):
    raise FileExistsError("Word list file does not exist")
    run = False
    error_text.append("Word list file does not exist")


if run:
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

else:
    if os.path.isfile(OUTPUT_FILE_NAME):
        with open(OUTPUT_FILE_NAME, "w") as file:
            file.write(error_text)
    else:
        with open(OUTPUT_FILE_NAME, "x") as file:
            file.write(error_text)

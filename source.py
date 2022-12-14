import random as rd
import os

INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"
WORD_LIST_FILE_NAME = "wordlist.txt"

wordlist = []
error_text = []
run = True

if not os.path.isfile(INPUT_FILE_NAME):
    run = False
    error_text.append("Input file does not exist.\nPlease create a file named 'input.txt' in the same folder as this program.")
if not os.path.isfile(WORD_LIST_FILE_NAME):
    run = False
    error_text.append("Wordlist file does not exist.\nPlease create a file named 'wordlist.txt' in the same folder as this program.")

if run:
    with open(WORD_LIST_FILE_NAME, "r") as file:
        text = file.read().splitlines()
        split_data = []
        for line in text:
            split_data.append(line.split('='))

    for line in split_data:
        replacement_words = line[0].split(";")
        replaced_words = line[1].split(";")

        wordlist.append([{"replacement_words": replacement_words, "replaced_words": replaced_words}])

    with open(INPUT_FILE_NAME, "r") as file:
        text = file.read().splitlines()

    new_text = []

    for line in text:
        new_line = []
        for word in line.split(" "):
            replaced = False
            for item in wordlist:
                if word in item[0]["replaced_words"]:
                    new_line.append(rd.choice(item[0]["replacement_words"]))
                    replaced = True
            if not replaced:
                if "be" in word:
                    new_line.append(word.replace("be", "BE"))
                elif "Be" in word:
                    new_line.append(word.replace("Be", "BE"))
                elif "bE" in word:
                    new_line.append(word.replace("bE", "BE"))
                else:
                    new_line.append(word)
        new_text.append(" ".join(new_line))

    if os.path.isfile(OUTPUT_FILE_NAME):
        with open(OUTPUT_FILE_NAME, "w") as file:
            for line in new_text:
                file.write(line)
                file.write("\n")
    else:
        with open(OUTPUT_FILE_NAME, "x") as file:
            for line in new_text:
                file.write(line)
                file.write("\n")


else:
    if os.path.isfile(OUTPUT_FILE_NAME):
        with open(OUTPUT_FILE_NAME, "w") as file:
            for error in error_text:
                file.write(error + "\n")
            file.write("For more information, please refer to the README file.")
    else:
        with open(OUTPUT_FILE_NAME, "x") as file:
            for error in error_text:
                file.write(error + "\n")
            file.write("For more information, please refer to the README file.")

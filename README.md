# tekst-forBEdrer

## **wordlist.txt** :

  List of words that should be replaced, and the words to replace them with.
  The list is formatted such that each line hold one or more words to be replaced, and one or more words to replace them with.
  
    REPLACEMENT_WORD_01;REPLACEMENT_WORD_02=REPLACE_WORD_01;REPLACE_WORD_02
  
  This is an example of a single line in the wordlist.txt file. Word(s) you wish to have replaced are behind the "=" 
  and the words you wish to replace them with are infront of the "=". The indevidual words on each side is separated by a ";"
  Places and sumbols other then "=" and ";" can be used in the words, making phrases or full sentences posible.

## input.txt :

  This text file is the text you wish to have the words replaced in. The text file should be in the same folder as the wordlist.txt file.

## output.txt :

  This text file is the output of the program. It will be created in the same folder as the wordlist.txt file.
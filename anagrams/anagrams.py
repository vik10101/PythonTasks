# Anagram is a word play of rearranging the letters of a word so the new word exists.
# You have to use all original letters exactly once. The result is a list of alphabetically sorted words.

import os

def check(word, file_name):

    anagrams = []

    # Here we open the file using the absolute path to the exact file in read mode.
    with open(os.path.abspath(file_name), 'r', encoding="utf-8") as file:

        # For every line in the file we check if the word is anagram.
        for line in file:

            is_anagram = True
            line = line.strip()

            # First we check if the length of the two words is the same. If it is not or if we find the exact same word
            # there is no point to check further so we skip to the next word.
            if (len(word) != len(line)) or (word == line):
                continue

            # We check if all the letters from the given word are met in the one from the file.
            for char in word:

                if char not in line:
                    is_anagram = False

            if is_anagram:
                anagrams.append(line)

    return anagrams

def main():

    word = input("Enter the word: ")
    file_name = input("Enter the name of the file: ")

    # Calling for the function "check" as we are passing the word and the file name we want and then we sort the result.
    result = check(word, file_name)
    result.sort()

    for word in result:
        print(word)

if __name__ == "__main__":
    main()

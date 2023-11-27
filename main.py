import string

with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    words = file_contents.split()

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document\n")

    letter_count = {}
    for letter in string.ascii_lowercase:
        print(f"The '{letter}' character was found {file_contents.lower().count(letter)} times")
    print("--- End report ---")

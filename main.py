def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print (count_letters(file_contents))

def count_words(string):
    words = string.split()
    return (len(words))

def count_letters(string):
    # Counts upper and lower case the same
    alphabet = {
        'a':0,
        'b':0,
        'c':0,
        'd':0,
        'e':0,
        'f':0,
        'g':0,
        'h':0,
        'i':0,
        'j':0,
        'k':0,
        'l':0,
        'm':0,
        'n':0,
        '0':0,
        'p':0,
        'q':0,
        'r':0,
        's':0,
        't':0,
        'u':0,
        'v':0,
        'w':0,
        'x':0,
        'y':0,
        'z':0}
    for i in string.lower():
        if i in alphabet:
            alphabet[i] = alphabet[i] + 1
    return alphabet
main()
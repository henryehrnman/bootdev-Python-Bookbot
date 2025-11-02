from stats import get_num_words
from stats import num_for_char
def main():
    get_book_text("books/frankenstein.txt")
    get_num_words("books/frankenstein.txt")
    dick = num_for_char("books/frankenstein.txt")
    print(dick)


def get_book_text(filepath) :
    with open(filepath) as f:
        file_contents = f.read()
        print(file_contents)


main()


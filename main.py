#import system arguments from CLI
import sys

#imports from stats.py
from stats import get_num_words
from stats import num_for_char
from stats import split_dictionary


def main():
    length_of_arg = len(sys.argv)
    if length_of_arg != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    #get filepath and store the file contents in a string
    main_filepath = sys.argv[1]
    book = get_book_text(main_filepath)

    #create the dictionary with the number of each char in the book
    dic = num_for_char(book)
    #get the sorted list of dictionaries storing the char and the count of the char
    sorted_list = split_dictionary(dic)
    #print the report
    print_report(main_filepath, sorted_list)

#reads the file and stores it as a string
def get_book_text(filepath) :
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

#analyzes the file and prints the report of how many different characters
def print_report(main_filepath, sorted_list) :
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {main_filepath}")
    print("----------- Word Count ----------")
    num_of_words = get_num_words(main_filepath)
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")
    print("============= END ===============")


#call to main method
main()


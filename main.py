from stats import get_num_words
from stats import num_for_char
from stats import split_dictionary

def main():
    #get_book_text("books/frankenstein.txt")
    #get_num_words("books/frankenstein.txt")
    dic = num_for_char("books/frankenstein.txt")
    #print(dic)
    sorted_list = split_dictionary(dic)
    print_report(sorted_list)



def get_book_text(filepath) :
    with open(filepath) as f:
        file_contents = f.read()
        print(file_contents)

def print_report(sorted_list) :
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    num_of_words = get_num_words("books/frankenstein.txt")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha():
            print(f"{ch}: {count}")
    print("============= END ===============")

main()


def get_num_words(filepath) :
    with open(filepath) as f:
            file_contents = f.read()
    num_of_words = len(file_contents.split())
    print(f"Found {num_of_words} total words")

def num_for_char(filepath) :
    with open(filepath) as f:
        file_contents = f.read()
    words = file_contents.split()
    char_dictionary = {}
    for word in words :
        for char in word :
            #check for char then add to dictionary if need
            pass




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
            lowercase_char = char.lower()
            charKey = char_dictionary.get(lowercase_char, -1)
            if charKey == -1:
                char_dictionary[lowercase_char] = 1
            else :
                char_dictionary[lowercase_char] = charKey + 1
    return char_dictionary





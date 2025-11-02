def get_num_words(filepath) :
    with open(filepath) as f:
            file_contents = f.read()
    num_of_words = len(file_contents.split())
    return num_of_words

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
def sort_on(item):
    return item["num"]

def split_dictionary(char_dictionary) :
    items = char_dictionary.items()
    list_of_items = []
    for char, num in items:
        new_dictionary = {"char" : char , "num": num}
        list_of_items.append(new_dictionary)
    list_of_items.sort(reverse=True, key=sort_on)
    return list_of_items






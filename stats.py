#gets the number of words in file_contents
def get_num_words(file_contents) :
    num_of_words = len(file_contents.split())
    return num_of_words

#creates a dictionary linking all the different characters to how many times it shows up in the file
def num_for_char(file_contents) :
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

#returns the value of item and item is the count of char
def sort_on(item):
    return item["num"]

#splits the dictionary into a list containing dictionaries of each char and its count
#the list is sorted by the count of each char
def split_dictionary(char_dictionary) :
    items = char_dictionary.items()
    list_of_items = []
    for char, num in items:
        new_dictionary = {"char" : char , "num": num}
        list_of_items.append(new_dictionary)
    list_of_items.sort(reverse=True, key=sort_on)
    return list_of_items






def read_file(filepath):
    # open the file and set a variable as the string returned by reading the file
    with open(filepath) as f:
        text = f.read()
    return text

def count_words(text):
    # split into list of words
    word_list = text.split()
    # check the length of the list
    word_count = len(word_list)
    return word_count

def sort_on(dict):
    return dict["num"]

def count_letters(text):
    # prep an empty dictionary for the letter counts and lower the letter cases
    letter_counts = {}
    lowered_text = text.lower()
    # iterate over every letter
    for letter in lowered_text:
        # check if the letter's already in the dictionary, if so increment count by 1
        if letter in letter_counts:
            letter_counts[letter] += 1
        # if it's not, add the letter to the dictionary as key, with count initially at 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def print_letter_counts(letter_counts):
    # create an empty list to contain the split dictionaries
    letters_list = []
    # iterate over each key in the letter counts dictionary
    for letter in letter_counts:
        # check if it's an alphabetical character, if so create a new dictionary
        if letter.isalpha() == True:
    # key "name" is letter counts' key and "num" is letter counts' value
            character_dict = {}
            character_dict["name"] = letter
            character_dict["num"] = letter_counts[letter]
            # append dictionary to list
            letters_list.append(character_dict)
    # sort the list using sort_on key defined above
    letters_list.sort(reverse=True, key=sort_on)
    # iterate over each dictionary in list and print out the relevant values
    for character in letters_list:
        letter = character["name"]
        count = character["num"]
        print(f"The '{letter}' character was found {count} times")

def main():
    # do I need a function to somehow set the filepath dynamically or is it ok to hardcode it?
    filepath = "books/frankenstein.txt"
    # call function to get the file contents
    text = read_file(filepath)
    # call functions to count stuff
    word_count = count_words(text)
    letter_counts = count_letters(text)
    # print the counted stuff
    print(f"- - Report of {filepath} - -")
    print()
    print(f"{word_count} words found in the document")
    print()
    print_letter_counts(letter_counts)
    print()
    print("- - End of report - -")

main()
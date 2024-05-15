# read_file() opens the passed file, reads contents to a variable,
# and splits those contents into a word list that can be parsed downstream;
# returns text (string), word_list (list of strings)
def read_file(filepath):
    with open(filepath) as f:
        text = f.read()
        word_list = text.split()
    f.close()
    return word_list

# get_distinct_words() creates a dictionary with key: each string from a passed
# list of strings, and value: the count associated with each of those words
# TODO: this needs to strip punctuation somehow
def get_distinct_words(word_list):
    distinct_words = {}
    for word in word_list:
        lowered_word = word.lower()
        if lowered_word in distinct_words:
            distinct_words[lowered_word] += 1
        else:
            distinct_words[lowered_word] = 1
    return distinct_words

# count_totals() takes a passed list of strings and a passed
# dictionary of distinct words and counts the totals of each; returns total_word_count
# (integer) and total_distinct_words (integer)
def count_totals(word_list, distinct_words):
    total_word_count = len(word_list)
    total_distinct_words = 0
    for word in distinct_words:
        total_distinct_words += 1
    return total_word_count, total_distinct_words

# sort_on() defines a sorting method associated with a passed dictionary,
# requires that the passed dictionary include a key labeled "num" on which to sort;
# returns the value associated with "num" key
def sort_on(dict):
    return dict["num"]

# get_sorted_distinct_words() takes a dictionary of words and counts per
# word and converts that into a list where each item is a dictionary with keys
# "name" associated with each word from the original dictionary and "num"
# associated with the respective count; then sorts that list of dictionaries using
# the sort_on method defined above and returns the sorted list
def get_sorted_distinct_words(distinct_words):
    sorted_distinct_words = []
    for word in distinct_words:
        word_dict = {}
        word_dict["name"] = word
        word_dict["num"] = distinct_words[word]
        sorted_distinct_words.append(word_dict)
    sorted_distinct_words.sort(reverse=True, key=sort_on)
    return sorted_distinct_words

# write_report() is passed a filepath where it will write a report, a filepath
# indicating what text is reported on, and multiple values calculated by the
# evaluative functions above, including total word count, count of total distinct
# words, and the sorted list of each distinct word's respective count. It writes
# a formatted report to a text file and prints to the terminal a notification
# indicating where that file is.
def write_report(report_filepath, source_filepath, total_word_count, total_distinct_words, sorted_distinct_words):
    with open(report_filepath, "w") as f:
        f.write(f"- - Report of Words in {source_filepath} - -\n")
        f.write("\n")
        f.write(f"The text is {total_word_count} words long.\n")
        f.write(f"The text uses {total_distinct_words} distinct words.\n")
        f.write("\n")
        for word in sorted_distinct_words:
            f.write(f"The word '{word['name']}' occurs {word['num']} times.\n")
        f.write("\n")
        f.write("- - End of report - -")
    f.close()
    print(f"Report written to {report_filepath}")

# main() starts by defining what file to evaluate, calls a sequence of functions
# to read, parse, and count words within that file, takes the outputs of those
# functions and prints them to the terminal in a formatted report
# TODO: make the filepath user entry in the terminal instead of hardcoded
# TODO: output to a text file report instead of to terminal
def main():
    source_filepath = "books/frankenstein.txt"
    report_filepath = "reports/frankenstein_report.txt"
    word_list = read_file(source_filepath)
    distinct_words = get_distinct_words(word_list)
    sorted_distinct_words = get_sorted_distinct_words(distinct_words)
    total_word_count, total_distinct_words = count_totals(word_list, distinct_words)
    # print the counted stuff
    write_report(report_filepath, source_filepath, total_word_count, total_distinct_words, sorted_distinct_words)

main()
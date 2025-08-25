from stats import get_word_count, get_char_count, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:   
        file_contents = f.read()
    print (file_contents)
    

    

    
# get_book_text("books/frankenstein.txt")
# get_word_count("books/frankenstein.txt")
# get_char_count("books/frankenstein.txt")
sort_dict(sys.argv[1])
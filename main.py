from stats import get_word_count, get_char_count, sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:   
        file_contents = f.read()
    print (file_contents)
    

    

    
# get_book_text("books/frankenstein.txt")
# get_word_count("books/frankenstein.txt")
# get_char_count("books/frankenstein.txt")
sort_dict("books/frankenstein.txt")
def get_word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
    print ( f"{num_words} words found in the document")
    
def get_char_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        
        file_single_chars = list(file_contents)
        
        char_count = {}
        
        for char in file_single_chars:
            if char.isalpha():
                char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1
            
        print (char_count)
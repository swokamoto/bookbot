def get_word_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        num_words = len(file_contents.split())
    return num_words

def get_char_count(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        
        file_single_chars = list(file_contents)
        
        char_count = {}
        
        for char in file_single_chars:
            if char.isalpha():
                char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1

        return char_count

def sort_dict(path_to_file):
    
    word_count = get_word_count(path_to_file)
    char_count = get_char_count(path_to_file)
    sortable_count = []

    print ("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")
    print ("----------- Word Count ----------")
    print (f"Found {word_count} total words")
    print ("--------- Character Count -------")

    
    for char in char_count:
        if char.isalpha():

            sortable_count.append({"char": f"{char}", "num": f"{char_count[char]}"})

    sortable_count.sort(key=lambda x: int(x['num']), reverse=True)
    

    for char in sortable_count:
        print (f"{char['char']}: {char['num']}")

    print ("============= END ===============")
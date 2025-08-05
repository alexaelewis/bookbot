def word_counter(text_block):
    words = text_block.split()

    return(len(words))

def character_counter(text_block):
    text_block_lower = text_block.lower()
    char_set = list(set(text_block_lower))
    char_set.sort()

    char_dict = {}
    for character in char_set:
        char_dict[character] = text_block_lower.count(character)

    return(char_dict)

def sort_on(items):
    return items["num"]

def sort_char_dict(char_dict):
    dict_list = []
    for item in char_dict:
        dict_list.append({"char": item, "num": char_dict[item]})

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

def print_report(book_file, word_count, sorted_char_dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_dict_list:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")
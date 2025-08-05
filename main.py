import sys

from stats import word_counter, character_counter, sort_char_dict, print_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_file = sys.argv[1]
        book_text = get_book_text(book_file)
        word_count = word_counter(book_text)

        print(f"{word_count} words found in the document")

        char_dict = character_counter(book_text)
        print(char_dict)

        sorted_char_dict_list = sort_char_dict(char_dict)
        print(sorted_char_dict_list)

        print_report(book_file, word_count, sorted_char_dict_list)

main()
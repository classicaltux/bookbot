import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import get_char_count
from stats import sort_chars_by_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    char_count = get_char_count(book_text)
    char_sort = sort_chars_by_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in char_sort:
        char = char_dict["char"]
        if char.isalpha():
            count = char_dict["count"]
            print(f"{char}: {count}")
    print(f"============= END ===============")

main()
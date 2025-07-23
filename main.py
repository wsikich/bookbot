import sys
input = sys.argv
def system_input():
    if len(input) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
system_input()
def get_book_text(book):
    with open(book) as b:
        book_string = b.read()
        return book_string
from stats import get_word_count
from stats import get_character_counts
from stats import get_sorted_dicts
book_text = get_book_text(input[1])
word_count = get_word_count(book_text)
character_counts = get_character_counts(book_text)
sorted_dicts = get_sorted_dicts(character_counts)
def intro():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input[1]}...")
def sorted_character_list():
    for dict in sorted_dicts:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
def main():
    intro()
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_character_list()
    print("============= END ===============")
    
main()
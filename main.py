from stats import text_to_words, count_characters, sort_dic
# im porting a function from stats.py file in the same folder as main.py
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_content = get_book_text(path)
    num_words = text_to_words(book_content)
    character_count = count_characters(book_content)
    sorted_dictionary = sort_dic(character_count)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dictionary:
        if item['char'].isalpha():
            print(f'{item['char']}: {item['num']}')
    print("============= END ===============")
    
main()
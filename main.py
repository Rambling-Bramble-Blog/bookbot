import sys
from stats import get_num_words,  get_num_char, sort_char_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)    
    num_char_dict = get_num_char(book_text)
    sorted_char_dict = sort_char_dict(num_char_dict)

    
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    for i in sorted_char_dict:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()

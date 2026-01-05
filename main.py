from stats import get_num_words,  get_num_char

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    frankenstein_rel_path = "books/frankenstein.txt"
    
    book_text = get_book_text(frankenstein_rel_path)
    num_words = get_num_words(book_text)    
    num_char = get_num_char(book_text)
    
    print(f"Found {num_words} total words. \n {num_char}")

main()

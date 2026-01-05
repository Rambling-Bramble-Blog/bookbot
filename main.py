def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def word_count(file_text):
    word_count = 0
    file_words = file_text.split()
    
    for word in file_words:
        word_count += 1
        
    return word_count
    
def main():
    frankenstein_rel_path = "books/frankenstein.txt"
    
    num_words = word_count(get_book_text(frankenstein_rel_path))    
    
    print(f"Found {num_words} total words")

main()

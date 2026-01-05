def get_num_words(file_text):
    word_count = 0
    file_words = file_text.split()
    
    for word in file_words:
        word_count += 1
        
    return word_count

def get_num_char(file_text):
    char_count_dict = {}
    
    for char in file_text.lower():
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
        
    return char_count_dict
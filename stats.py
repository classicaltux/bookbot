def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_char_count(book_text): 
    char_count = {}
    chars = book_text.lower()#lower case all the characters
    for char in chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_chars_by_count(char_count):
    char_list = []
    for char , count in char_count.items():
        char_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list

    
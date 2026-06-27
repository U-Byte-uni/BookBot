def count_words(book_text):
    words = book_text.split()
    return len(words)



def count_characters(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count



def sort_on(count_dict: tuple[str,int]) -> int:
    return count_dict[1]

def sort_count(count_dict):
    sorted_count = sorted(count_dict.items(),key=sort_on,reverse=True)
    return sorted_count

def count_words(book_text):
    words = book_text.split()
    return len(words)

# Numbers of time each character appears in the book including spaces and punctuation 
# Use lower_case to avoid duplicates
# output should be {'p': 6121, 'r': 20818, 'o': 25225, ...

def count_characters(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
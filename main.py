from stats import count_words
from stats import count_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    path = "/home/Uzair/VS Code/Bootdev/BookBot/books/frankenstein.txt"
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
    char_counts = count_characters(book_text)
    print(f"Found {len(char_counts)} unique characters")
    print(char_counts)
    for char, count in char_counts.items():
        print(f"The '{char}' character was found {count} times")

main()
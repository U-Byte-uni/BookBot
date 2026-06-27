import sys
from stats import count_words
from stats import count_characters
from stats import sort_count

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(path,word_count,char_counts,sorted_count):
    print("======= Book Report =======")
    print(f"Analyzing book at path: {path}")
    print("------------ Word Count ------------")
    print(f"Found {word_count} total words")
    print("------------ Character Count ------------")
    for char,count in sorted_count:
        if char.isalpha():
            print(f"{char}: {count}")
        
    print("=========== END OF REPORT ===========")

def main():
 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_count = sort_count(char_counts)
    print_report(path, word_count, char_counts, sorted_count)
   

main()
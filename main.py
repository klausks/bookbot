from stats import count_words, count_char_occurrences, sorted_char_count
from sys import argv, exit

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    book_file_path = argv[1]
    book_text = get_book_text(book_file_path)
    words_count = count_words(book_text)
    report(book_file_path, words_count, sorted_char_count(count_char_occurrences(book_text)))

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def report(book_file_path, word_count, sorted_char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")
    for char in sorted_char_count:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()
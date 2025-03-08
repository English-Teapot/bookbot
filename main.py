import sys

# Import the work count and character count function
from stats import word_count, character_count, format_display

# Gets the book text and converts to string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents
     

def main():
    # Prints out the book
    # print(get_book_text("books/frankenstein.txt"))

    # Gets Word count in a single line
    # print(word_count(get_book_text("books/frankenstein.txt")))

    # Gets Word count readable 
    #file_path = "books/frankenstein.txt"

    # Exit program and give usage message if incorrect input
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Set the filepath
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    words = word_count(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    sorted_chars = format_display(character_count(book_text))
    for char_count in sorted_chars:
        char = char_count["char"]
        count = char_count["count"]
        print(f"{char}: {count}")

    print("============= END ===============")


main()
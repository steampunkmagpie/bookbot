import sys

from stats import word_count

from stats import char_count

from stats import sorted_list

if len(sys.argv) <= 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text(sys.argv[1])
    num_words = word_count(book)
    char=char_count(book)
    sorted=sorted_list(char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()
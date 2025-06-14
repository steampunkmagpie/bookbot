from stats import word_count

from stats import char_count

from stats import sorted_list

file_path = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text(file_path)
    num_words = word_count(book)
    char=char_count(book)
    sorted=sorted_list(char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()
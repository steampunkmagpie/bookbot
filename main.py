from stats import word_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text("books/frankenstein.txt")
    num_words = word_count(book)
    print(f"{num_words} words found in the document")

main()
def word_count(book):
    words = book.split()
    count = 0
    for i in words:
        count += 1
        num_words = count
    return num_words

def char_count(book):
    char = {}
    book=str.lower(book)
    words = book.split()
    for word in words:
        for i in word:
            if i in char:
                char[i] +=1
            else:
                char[i]=1
    return char
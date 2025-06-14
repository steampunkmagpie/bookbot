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

def sorted_list(char):
    sorted = []
    for item in char:
        if item.isalpha() == True:
            sorted.append({"char": item, "num" :char[item]})
    def full_sort(sorted):
        return sorted["num"]
    sorted.sort(reverse=True, key=full_sort)
    return sorted







    

    
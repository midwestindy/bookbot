def count_words(text_to_count):
    counted_words = 0
    words = text_to_count.split()
    for word in words:
        counted_words += 1
    return counted_words

def main():
    book_to_read = 'books/frankenstein.txt'
    text_from_book = read_book(book_to_read)
    counted_text = count_words(text_from_book)
    
    print(f'{counted_text} is the total word count')

def read_book(path_to_book):
    with open(path_to_book) as boo:
        return boo.read()
    #print(set(files_content.lower()))

 

main()

def count_words(text_to_count):
    counted_words = 0
    words = text_to_count.split()
    for word in words:
        counted_words += 1
    return counted_words


def main():
    book_path = 'books/frankenstein.txt'
    after_read = read_book(book_path)
    after_count = count_words(after_read)
    print(f'{after_read}\n the above book has {after_count} words in it.\n')
    after_count_char = character_numbers(after_read)
    created_list_of_dicts = create_list_of_dicts(after_count_char)
    sorted_list = sort_on(created_list_of_dicts)
    print_sorted_list(sorted_list, created_list_of_dicts)


def read_book(path_to_book):
    with open(path_to_book) as boo:
        return boo.read()


def character_numbers(text_from_book):
    convert_to_set = set(text_from_book.lower())
    converted_text = {}
    for converted in convert_to_set:
        converted_text[converted] = 0
        for character in text_from_book:
            if converted == character:
                converted_text[converted] += 1
    return converted_text


def create_list_of_dicts(dict_to_convert):
    converted_dicts = []
    for key_value in dict_to_convert:
        empty_dict = {}
        if key_value.isalpha():
            empty_dict[key_value] = dict_to_convert[key_value]
            converted_dicts.append(empty_dict)
    return converted_dicts


def sort_on(input_stream):
    list_of_keys = []
    for index in range(len(input_stream)):
        for key in input_stream[index]:
            list_of_keys.append(key)
    list_of_keys.sort()
    return list_of_keys


def print_sorted_list(list_to_print, dict_to_use):
    for char in list_to_print:
        for item in dict_to_use:
            if char in item:
                print(f"The '{char}' character was found {item[char]} times")


main()

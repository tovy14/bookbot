
def read_content(path):
    with open(path) as file:
        return file.read()


def word_counter(input_string):
    counter = 0
    words = input_string.split()
    for word in words:
        counter += 1
    return counter


def count_characters(input_string):
    character_count = {}
    for char in input_string.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


def main():
    book_path = "books/frankenstein.txt"
    book_string = read_content(book_path)
    print(word_counter(book_string))
    print(count_characters(book_string))


main()

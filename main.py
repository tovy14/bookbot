
def read_content(path):
    with open(path) as file:
        return file.read()


def word_counter(input_string):
    counter = 0
    words = input_string.split()
    for word in words:
        counter += 1
    return counter


def main():
    book_path = "books/frankenstein.txt"
    book_string = read_content(book_path)
    print(word_counter(book_string))


main()

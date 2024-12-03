
def read_content(path):
    with open(path) as file:
        return file.read()


def main():
    book_path = "books/frankenstein.txt"
    print(read_content(book_path))


main()

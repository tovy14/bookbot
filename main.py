
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


def print_report(input_dict):

    for char in input_dict:
        print(f"The '{char}' character was found {input_dict[char]} times")


def main():
    book_path = "books/frankenstein.txt"
    book_string = read_content(book_path)
    # print(word_counter(book_string))
    # print(count_characters(book_string))
    print(f"-- Begin report of books/frankenstein.txt ---")
    print(f"{word_counter(book_string)} words found in the document\n")
    print_report(count_characters(book_string))
    print(f"\n--- End report ---")
    print(word_counter(book_string), count_characters(book_string))


main()

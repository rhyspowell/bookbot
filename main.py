def sort_on(dict):
    return dict["num"]


def main():
    number_of_words = 0

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lines = file_contents.split()
        number_of_words += len(lines)

        char_count = {}

        for char in file_contents:
            lower_char = char.lower()
            if lower_char in char_count:
                char_count[lower_char] = char_count[lower_char] + 1
            else:
                char_count[lower_char] = 1

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{number_of_words} words found in the document")
        print("")
        char_count = {
            k: v
            for k, v in sorted(
                char_count.items(), key=lambda item: item[1], reverse=True
            )
        }
        for key, val in char_count.items():
            if key.isalpha():
                print(f"The '{key}' character was found {val} times")

        print("--- End report ---")


main()

def sort_on(dict):
    return dict["num"]


def get_num_words(book_name):
    number_of_words = 0

    with open(book_name) as f:
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

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_name}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("----------- Character Count ----------")
        char_count = {
            k: v
            for k, v in sorted(
                char_count.items(), key=lambda item: item[1], reverse=True
            )
        }
        for key, val in char_count.items():
            if key.isalpha():
                print(f"{key}: {val}")

        print("============= END ===============")

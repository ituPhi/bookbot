from stats import count_string_letters, count_words, sort_by_character_count
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        filecontents = f.read()
        return filecontents


def print_letters(items):
    letters = ""
    for i in items:
        if i["char"].isalpha() == False:
            continue
        else:
            letters += f"{i['char']}: {i['num']}\n"
    return letters


def report(word_count, letter_list, filepath):
    header = "============ BOOKBOT ============"
    word_count_header = "----------- Word Count ----------"
    character_count_header = "--------- Character Count -------"
    word_count_message = f"Found {word_count} total words"
    filepath_message = f"Analyzing book found at {filepath}..."
    closing_message = "============= END ==============="

    final_report = f"""
{header}\n
{filepath_message}\n
{word_count_header}\n
{word_count_message}\n
{character_count_header}\n
{letter_list}\n
{closing_message}

    """
    print(final_report)
    return final_report


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    letter_count = count_string_letters(book_text)
    sorted_letter_count = sort_by_character_count(letter_count)
    letter_list = print_letters(sorted_letter_count)
    final_report = report(word_count, letter_list, filepath)

    return


main()

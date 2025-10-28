from typing_extensions import Dict


def count_words(file_text):
    text_split = file_text.split()
    num_words = len(text_split)
    # print(f"Found {num_words} total words")
    return num_words


def count_string_letters(book_text):
    normalized_text = book_text.lower()
    letter_count_pairs = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
        " ": 0,
        "!": 0,
        '"': 0,
        "#": 0,
        "$": 0,
        "%": 0,
        "&": 0,
        "'": 0,
        "(": 0,
        ")": 0,
        "*": 0,
        "+": 0,
        ",": 0,
        "-": 0,
        ".": 0,
        "/": 0,
        ":": 0,
        ";": 0,
        "<": 0,
        "=": 0,
        ">": 0,
        "?": 0,
        "@": 0,
        "[": 0,
        "\\": 0,
        "]": 0,
        "^": 0,
        "_": 0,
        "`": 0,
        "{": 0,
        "|": 0,
        "}": 0,
        "~": 0,
    }

    for c in normalized_text:
        if c in letter_count_pairs:
            letter_count_pairs[c] += 1

    # print(letter_count_pairs)
    return letter_count_pairs


def sort_by_character_count(letter_count_pairs: Dict):
    def sort_on(items):
        return items["num"]

    list = []
    for key in letter_count_pairs:
        dict = {"char": key, "num": letter_count_pairs[key]}
        list.append(dict)

    list.sort(reverse=True, key=sort_on)
    # print(list)
    return list

# 2022 A Jarman
from typing import List


def word_reverser_builtins(phrase: str) -> str:
    """take a given string and reverse the order of the words.
    You may assume that the string is a sentence that contains only letters and spaces,
    with all words separated by one space.For example, word_reverser("Codecademy rules")
    should return "rules Codecademy" and word_reverser("May the Fourth be with you")
    should return "you with be Fourth the May".

    Args:
        phrase (str): the string is a sentence that contains only letters and spaces

    Returns:
        str: phrase with the order of words reversed.
    """

    # approach here is to identify

    # split into list of strings by empty space character
    words: List[str] = phrase.split(" ")  # O(?)
    words_reversed: List[str] = reversed(words)  # O(?)
    return " ".join(words_reversed)

"""This module is a collection of string algorithms in various implementations"""
from typing import List


class WordReversers:
    """
    Collection of word reversing methods/functions
    Inspired by Codeacademy Jan 2022
    """

    @staticmethod
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
        # added a comment here for demo

        # split into list of strings by empty space character
        words: List[str] = phrase.split(" ")  # O(?)
        words_reversed: List[str] = reversed(words)  # O(?)
        return " ".join(words_reversed)

    @staticmethod
    def word_reverser_iterative(phrase: str) -> str:
        """take a given string and reverse the order of the words.
        You may assume that the string is a sentence that contains only letters and spaces,
        with all words separated by one space.For example, word_reverser("Codecademy rules")
        should return "rules Codecademy" and word_reverser("May the Fourth be with you")
        should return "you with be Fourth the May".

        ## TIME COMPLEXITY:
        - max O(6n) + 3x
        - min O(3n) + 3x
        - generally (On)

        ## SPACE COMPLEXITY O(2n):
        - two strings created of n length

        Args:
            phrase (str): the string is a sentence that contains only letters and spaces

        Returns:
            str: phrase with the order of words reversed.
        """

        # use empty string and append words from end
        reversed_phrase: str = ""  # O(1), (1x)
        end_of_word: int = len(phrase)  # O(1), (2x)
        i: int = end_of_word - 1  # O(1), 3x
        # iterate through phrase backwards
        while i >= 0:  # O(n) where n is length of string
            if phrase[i] == " ":  # O(2n)
                new_word = phrase[i + 1 : end_of_word]  # O(2n)
                new_word += " "  # O(3n)
                reversed_phrase += new_word  # O(4n)
                end_of_word = i  # O(5n)
            elif i == 0:
                new_word = phrase[i:end_of_word]  # O(2n)
                reversed_phrase += new_word  # O(3n)
            i -= 1  # O(6n)

        return reversed_phrase

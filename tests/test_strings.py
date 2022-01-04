"""Tests for various string algorithms"""
from typing import Callable
import pytest
from src.strings import WordReversers


class TestWordReversers:
    """Collection of tests for string reverse functions"""

    @pytest.mark.parametrize(
        "phrase, answer",
        [
            ("Hello World", "World Hello"),
            ("I am an antelope", "antelope an am I"),
            ("", ""),
            ("This is your life", "life your is This"),
        ],
    )
    @pytest.mark.parametrize(
        "function",
        [WordReversers.word_reverser_builtins, WordReversers.word_reverser_iterative],
    )
    def test_word_reverser_builtins(self, phrase: str, answer: str, function: Callable):
        """Tests word reverser function

        Args:
            phrase (str): phrase to be tested
            answer (str): correct answer to test case
        """
        assert function(phrase) == answer

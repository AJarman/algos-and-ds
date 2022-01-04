# 2022 A Jarman
import pytest
from src.strings import word_reverser_builtins

REVERSE_STRING_TEST_CASES = [
    ("Hello World", "World Hello"),
    ("I am an antelope", "antelope an am I"),
    ("",""),
]


@pytest.mark.parametrize("phrase, answer", REVERSE_STRING_TEST_CASES)
def test_word_reversers(phrase: str, answer: str):
    """Tests word reverser function

    Args:
        phrase (str): phrase to be tested
        answer (str): correct answer to test case
    """
    assert word_reverser_builtins(phrase) == answer

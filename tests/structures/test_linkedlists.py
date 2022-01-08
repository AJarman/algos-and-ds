"""Linked List tests"""
from typing import Any
import pytest

from src.structures.linkedlists import LinkedList


def node_values_for_tests():
    """Creates a list of possible node values for parameters

    Returns:
        List[Any]: possible node values
    """
    return [1, 3, 5, 7, "hello", None]


@pytest.mark.parametrize("node_value", node_values_for_tests())
def test_linkedlist_constructor(node_value: Any):
    """[summary]

    Args:
        node_value (Any): possible node value
    """

    new_linkedlist = LinkedList(head_value=node_value)
    assert new_linkedlist.head_node.value == node_value


@pytest.mark.parametrize("node_value", node_values_for_tests())
def test_linkedlist_raise_error_non_node_added(node_value: Any):
    """
    Raises an Error by setting a non-node as the head_node

    Args:
        node_value (Any): possible node value
    """
    new_linkedlist = LinkedList(head_value=node_value)
    with pytest.raises(TypeError):
        not_node = 3
        new_linkedlist.head_node = not_node

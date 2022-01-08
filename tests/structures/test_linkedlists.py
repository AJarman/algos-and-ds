"""Linked List tests"""
from typing import Any
import pytest

from src.structures.linkedlists import LinkedList


def node_values_for_tests():
    """Creates a list of possible node values for parameters

    Returns:
        List[Any]: possible node values
    """
    return [1, 3, 5, 7, "hello"]


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

@pytest.mark.parametrize("node_value", node_values_for_tests())
def test_linkedlist_add_to_head(node_value: Any):
    """
    Raises an Error by setting a non-node as the head_node

    Args:
        node_value (Any): possible node value
    """

    head_value = "potato"
    new_linkedlist = LinkedList(head_value=head_value)
    new_linkedlist.add_to_head(new_node_value=node_value)
    assert new_linkedlist.head_node.next_node.value == head_value
    assert new_linkedlist.head_node.value == node_value


def test_linkedlist__len__():
    """
    tests the length method/dunder method
    """

    new_linkedlist = LinkedList(head_value="testhead")
    for i in node_values_for_tests():
        new_linkedlist.add_to_head(i)
    assert len(new_linkedlist) == len(node_values_for_tests()) +1


@pytest.mark.parametrize("node_value", node_values_for_tests())
def test_linkedlist_remove_values(node_value:Any):
    """
    Testing the removed values (1) are removed.
    Args:
        node_value (Any): [description]
    """

    new_linkedlist = LinkedList(head_value="testhead")
    for i in node_values_for_tests():
        new_linkedlist.add_to_head(i)

    current_size = len(new_linkedlist)
    new_linkedlist.remove_node(node_value)
    assert len(new_linkedlist) == current_size -1
    
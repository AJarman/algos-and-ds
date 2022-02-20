"""Linked List tests"""
from typing import Any

import pytest
from src.structures.doublylinkedlist import DoublyLinkedList

from .test_nodes import node_values_for_tests


@pytest.mark.parametrize("node_value", node_values_for_tests())
def test_linkedlists_constructors(node_value: Any):
    """[summary]

    Args:
        node_value (Any): possible node value
    """

    new_doublelinkedlist = DoublyLinkedList(head_value=node_value)
    assert new_doublelinkedlist.head_node.value == node_value
    assert new_doublelinkedlist.tail_node.value == node_value


@pytest.mark.parametrize("node_value", node_values_for_tests())
def test_linkedlists_raise_error_non_node_added(node_value: Any):
    """
    Raises an Error by setting a non-node as the head_node

    Args:
        node_value (Any): possible node value
    """

    new_doublelinkedlist = DoublyLinkedList(head_value=node_value)

    with pytest.raises(TypeError):
        not_node = 3
        new_doublelinkedlist.head_node = not_node


@pytest.mark.parametrize("node_value", node_values_for_tests())
def test_linkedlist_add_to_head(node_value: Any):
    """
    Raises an Error by setting a non-node as the head_node

    Args:
        node_value (Any): possible node value
    """

    head_value = "potato"
    new_linkedlist = DoublyLinkedList(head_value=head_value)
    new_linkedlist.add_to_head(new_node_value=node_value)
    assert new_linkedlist.head_node.next_node.value == head_value
    assert new_linkedlist.head_node.value == node_value
    assert new_linkedlist.head_node.next_node.prev_node.value == node_value


def test_linkedlist__len__():
    """
    tests the length method/dunder method
    """

    new_linkedlist = DoublyLinkedList(head_value="testhead")
    for i in node_values_for_tests():
        new_linkedlist.add_to_head(i)
    assert len(new_linkedlist) == len(node_values_for_tests()) + 1


@pytest.mark.parametrize("node_value", node_values_for_tests())
def test_linkedlist_remove_values(node_value: Any):
    """
    Testing the removed values (1) are removed.
    Args:
        node_value (Any): [description]
    """

    new_linkedlist = DoublyLinkedList(head_value="testhead")
    val_counts = {}
    for i in node_values_for_tests():
        val_counts[i] = val_counts.get(i, 0) + 1
        new_linkedlist.add_to_head(i)

    current_size = len(new_linkedlist)
    new_linkedlist.remove_node(node_value)
    # len also checks links are in place
    assert len(new_linkedlist) == current_size - val_counts[node_value]


def test_linkedlist__str__():
    """
    Testing the __str__ function
    also tests superclass
    Args:
        node_value (Any): [description]
    """

    new_linkedlist = DoublyLinkedList(head_value="testhead")
    test_list = ["testhead"]
    for i in node_values_for_tests():
        new_linkedlist.add_to_head(i)
        test_list.append(i)

    assert isinstance(str(new_linkedlist), str)
    assert "(h)" in str(new_linkedlist)
    assert "(t)" in str(new_linkedlist)


@pytest.mark.parametrize("val1, val2, test_list", [
    (1, 2, [1, 2, 3, 4, 5, 6, 7]),
    (1, 7, [1, 2, 3, 4, 5, 6, 7]),
    (1, 4, [1, 2, 3, 4, 5, 6, 7]),
    (6, 4, [1, 2, 3, 4, 5, 6, 7]),
])
def test_linkedlist_swap_values(val1: Any,
                                val2: Any, test_list: list):
    """
    Testing the swap_values function
    Args:
        node_value (Any): [description]
    """

    for index, value in enumerate(test_list):

        if index == 0:
            new_linkedlist = DoublyLinkedList(head_value=value)
        else:
            new_linkedlist.add_to_head(value)

        if value == val1:
            val1_index = -1 - index
        elif value == val2:
            val2_index = -1 - index

    new_linkedlist.swap_nodes(val1, val2)
    assert val1 in new_linkedlist
    assert val2 in new_linkedlist
    assert new_linkedlist[val2_index].value == val1
    assert new_linkedlist[val1_index].value == val2

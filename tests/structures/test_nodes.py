"""Tests for nodes"""
from typing import Any, List

import pytest
from src.structures.nodes import SinglyLinkedNode


def node_values_for_tests() -> List[Any]:
    """[summary]

    Returns:
        List[Any]: [
    """
    return [1, 2, 3, 4, 5, 6, 7, "spam", None, "sausage"]


def list_of_nodes_for_tests() -> List[SinglyLinkedNode]:
    """[summary]

    Returns:
        List[SinglyLinkedNode]: [description]
    """
    return [SinglyLinkedNode(i) for i in node_values_for_tests()]


@pytest.mark.parametrize("value", node_values_for_tests())
def test_sll_node_constructor(value):
    """[summary]

    Args:
        value (any): [description]
    """
    the_next_node = SinglyLinkedNode("Dumbo")
    new_node = SinglyLinkedNode(value, next_node=the_next_node)

    # check instance is correct
    assert isinstance(new_node, SinglyLinkedNode)
    # check value is correct
    assert new_node.value == value
    #check linked value is correct
    assert new_node.next_node.value == "Dumbo"

@pytest.mark.parametrize("value", node_values_for_tests())
def test_sll_node_constructor_no_link(value):
    """[summary]

    Args:
        value (any): [description]
    """
    new_node = SinglyLinkedNode(value)
    # check instance is correct
    assert isinstance(new_node, SinglyLinkedNode)
    # check value is correct
    assert new_node.value == value


@pytest.mark.parametrize("value", node_values_for_tests())
def test_sll_node_get_value(value):
    """[summary]

    Args:
        value (any): [description]
    """
    new_node = SinglyLinkedNode(value)
    assert new_node.value == value


@pytest.mark.parametrize("value", node_values_for_tests())
def test_node_set_value(value):
    """[summary]

    Args:
        value (any): [description]
    """
    new_node = SinglyLinkedNode("tomato")
    new_node.value = value
    assert new_node.value == value


@pytest.mark.parametrize("next_node", list_of_nodes_for_tests())
@pytest.mark.parametrize("value", node_values_for_tests())
def test_sll_node_get_next_node(next_node, value):
    """[summary]

    Args:
        value (any): [description]
    """
    the_next_node = next_node
    next_value = next_node.value

    new_node = SinglyLinkedNode(value, next_node=the_next_node)

    # check instance is correct
    assert isinstance(new_node, SinglyLinkedNode)
    # check value is correct
    # check next node value is correct
    assert new_node.next_node.value == next_value
    assert isinstance(new_node.next_node, SinglyLinkedNode)


@pytest.mark.parametrize("value", node_values_for_tests())
def test_sll_node_set_next_node(value):
    """[summary]

    Args:
        value (any): [description]
    """
    # create node
    test_next_node = SinglyLinkedNode(value)
    # create 2nd node
    new_node = SinglyLinkedNode("tomato")
    #create link
    new_node.next_node = test_next_node

    assert new_node.next_node.value == value

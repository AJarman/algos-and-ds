"""Tests for nodes"""
import pytest
from src.structures.node import SingleLinkNode


def node_values_for_tests():
    return [1, 2, 3, 4, 5, 6, 7, "spam", None, "sausage"]


def list_of_nodes_for_tests():
    return [SingleLinkNode(i) for i in node_values_for_tests()]


@pytest.mark.parametrize("value", node_values_for_tests())
def test_sll_node_constructor(value):
    """[summary]

    Args:
        value (any): [description]
    """
    the_next_node = SingleLinkNode("Dumbo")
    new_node = SingleLinkNode(value, next_node=the_next_node)

    # check instance is correct
    assert isinstance(new_node, SingleLinkNode)
    # check value is correct
    assert new_node.get_value() == value


@pytest.mark.parametrize("value", node_values_for_tests())
def test_sll_node_get_value(value):
    """[summary]

    Args:
        value (any): [description]
    """
    new_node = SingleLinkNode(value)
    assert new_node.get_value() == value


@pytest.mark.parametrize("value", node_values_for_tests())
def test_sll_node_set_value(value):
    """[summary]

    Args:
        value (any): [description]
    """
    new_node = SingleLinkNode("tomato")
    new_node.set_value(value)
    assert new_node.get_value() == value


@pytest.mark.parametrize("next_node", list_of_nodes_for_tests())
@pytest.mark.parametrize("value", node_values_for_tests())
def test_sll_node_get_next_node(next_node, value):
    """[summary]

    Args:
        value (any): [description]
    """
    the_next_node = next_node
    next_value = next_node.get_value()

    new_node = SingleLinkNode(value, next_node=the_next_node)

    # check instance is correct
    assert isinstance(new_node, SingleLinkNode)
    # check value is correct
    # check next node value is correct
    assert new_node.get_next_node().get_value() == next_value
    assert isinstance(new_node.get_next_node(), SingleLinkNode)


@pytest.mark.parametrize("value", node_values_for_tests())
def test_sll_node_set_next_node(value):
    """[summary]

    Args:
        value (any): [description]
    """
    test_next_node = SingleLinkNode(value)
    new_node = SingleLinkNode("tomato")
    new_node.set_next_node(test_next_node)
    assert new_node.get_next_node().get_value() == value

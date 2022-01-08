"""Tests for nodes"""
from typing import Any, List

import pytest
from src.structures.nodes import DoubleLinkedNode, SinglyLinkedNode


def node_values_for_tests() -> List[Any]:
    """[summary]

    Returns:
        List[Any]: list of potential node values
    """
    return [1, 2, 3, 4, 5, 6, 7, "spam", "sausage"]


def list_of_nodes_for_tests() -> List[SinglyLinkedNode]:
    """[summary]

    Returns:
        List[SinglyLinkedNode]: [description]
    """
    return [SinglyLinkedNode(i) for i in node_values_for_tests()]

class TestSingleLinkedNode:
    """
    Tests for singly linked list
    """
    @staticmethod
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
        # check linked value is correct
        assert new_node.next_node.value == "Dumbo"

    @staticmethod
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

    @staticmethod
    @pytest.mark.parametrize("value", node_values_for_tests())
    def test_sll_node_constructor_invalid_link(value):
        """[summary]

        Args:
            value (any): [description]
        """
        the_next_node: Any = value
        # check instance raises error
        with pytest.raises(TypeError):
            SinglyLinkedNode(value, next_node=the_next_node)

    @staticmethod
    @pytest.mark.parametrize("value", node_values_for_tests())
    def test_sll_node_get_value(value):
        """[summary]

        Args:
            value (any): [description]
        """
        new_node = SinglyLinkedNode(value)
        assert new_node.value == value

    @staticmethod
    @pytest.mark.parametrize("value", node_values_for_tests())
    def test_node_set_value(value):
        """[summary]

        Args:
            value (any): [description]
        """
        new_node = SinglyLinkedNode("tomato")
        new_node.value = value
        assert new_node.value == value

    @staticmethod
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

    @staticmethod
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
        # create link
        new_node.next_node = test_next_node

        assert new_node.next_node.value == value


class TestDoubleLinkedNode:
    """
    Tests for double linked list
    """
    @staticmethod
    @pytest.mark.parametrize("value", node_values_for_tests())
    def test_dll_node_constructor(value):
        """[summary]

        Args:
            value (any): [description]
        """
        the_next_node = DoubleLinkedNode("Dumbo")
        the_prev_node = DoubleLinkedNode("Bambi")
        new_node = DoubleLinkedNode(value,
                                    next_node=the_next_node,
                                    prev_node=the_prev_node)

        # check instance is correct
        assert isinstance(new_node, DoubleLinkedNode)
        # check value is correct
        assert new_node.value == value
        # check linked value is correct
        assert new_node.next_node.value == "Dumbo"
        # check linked value is correct
        assert new_node.prev_node.value == "Bambi"


    @staticmethod
    @pytest.mark.parametrize("value", node_values_for_tests())
    def test_dll_node_constructor_no_links(value):
        """[summary]

        Args:
            value (any): [description]
        """
        new_node = DoubleLinkedNode(value)
        # check instance is correct
        assert isinstance(new_node, DoubleLinkedNode)
        # check value is correct
        assert new_node.value == value
        assert new_node.next_node is None
        assert new_node.prev_node is None

    @staticmethod
    @pytest.mark.parametrize("value", node_values_for_tests())
    def test_dll_node_constructor_invalid_link(value):
        """[summary]

        Args:
            value (any): [description]
        """
        the_next_node: Any = value
        # check instance raises error
        with pytest.raises(TypeError):
            DoubleLinkedNode(value, prev_node=the_next_node)

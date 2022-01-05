"""Linked List tests"""
import pytest

from src.structures.linkedlist import LinkedList

def node_values_for_tests():
    return [1,3,5,7,"hello",None]

@pytest.mark.parametrize("node_value", node_values_for_tests())
def test_linkedlist_constructor(node_value):

    new_linkedlist = LinkedList(head_value=node_value)
    assert new_linkedlist.head_node.get_value() == node_value


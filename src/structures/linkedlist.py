"""Linked List implementations"""
from typing import Any
from .node import SingleLinkNode


class LinkedList:
    """
    Implementation of a singly linked list
    """

    def __init__(self, head_value: Any):
        """[summary]

        Args:
            head_value (Any): [description]
        """
        self._head_node = SingleLinkNode(head_value)

    @property
    def head_node(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return self._head_node

    @head_node.setter
    def set_head_node(self, new_node):
        """[summary]

        Args:
            new_node ([type]): [description]

        Raises:
            TypeError: [description]
        """
        if isinstance(new_node, SingleLinkNode):
            self._head_node = new_node
        else:
            raise TypeError(
                f"new node: {str(new_node)} is not a compatible Node")

"""Linked List implementations"""
from typing import Any, Type
from .nodes import SinglyLinkedNode


class LinkedList:
    """
    Python Implementation of a singly linked list
    """

    def __init__(self, head_value: Any) -> None:
        """Constructor for Linkedlist, add a head valuee

        Args:
            head_value (Any): value of any type to be the head
        """
        self._head_node = SinglyLinkedNode(head_value)

    @property
    def head_node(self) -> Type[SinglyLinkedNode]:
        """Getter for head_node

        Returns:
            Type[SinglyLinkedNode]: the head node
        """
        return self._head_node

    @head_node.setter
    def head_node(self, new_node: Type[SinglyLinkedNode]) -> None:
        """
        Setter for head node, validates correct type

        Args:
            new_node (SinglyLinkedNode): New node which will be head_node

        Raises:
            TypeError: this is raised if new_node is not a SinglyLinkedNode
        """
        if isinstance(new_node, Type[SinglyLinkedNode]):
            self._head_node = new_node
        else:
            raise TypeError(
                f"new node: {str(new_node)} is not a compatible Node")

    def insert_beginning(self, new_node_value: Any) -> None:
        """
        Creates a new head node containing this value,
        updates the new head node to be linked to the old head node.

        Args:
            new_node_value (Any): create a new node with this value
        """
        # create a new node with this value
        new_node = SinglyLinkedNode(
            value=new_node_value, next_node=self.head_node)
        self.head_node = new_node

    # def remove_node(self, value_to_remove:Any)->None:

    #     # start at the head
    #     current_node = self.get_head_node()
    #     # if
    #     if current_node.value == value_to_remove:
    #         self.head_node = current_node.next_node
    #     else:
    #         while current_node: # is not None
    #             next_node = current_node.next_node
    #             if next_node and next_node.value == value_to_remove:
    #                 next_next_node = next_node.next_node
    #                 current_node.next_node = next_next_node
    #             current_node = next_next_node
    #             else:
    #             current_node = next_node

"""
Doublylinkedlist implementation
"""
from logging import getLogger
from typing import Any, List, Optional, Type

from .linkedlist import LinkedList
from .nodes import DoubleLinkedNode

logger = getLogger(__name__)


class DoublyLinkedList(LinkedList):
    """
    Python Implementation of a doubly linked list
    """

    # pylint: disable=super-init-not-called
    def __init__(self, head_value: Any) -> None:
        """Constructor for DoublyLinkedlist, add a head value

        Args:
            head_value (Any): value of any type to be the head
        """
        self.head_node = DoubleLinkedNode(value=head_value)
        self.tail_node = self.head_node

    @property
    def tail_node(self) -> Type[DoubleLinkedNode]:
        """Getter for head_node

        Returns:
            Type[DoubleLinkedNode]: the tail node
        """
        return self._tail_node

    @tail_node.setter
    def tail_node(self, new_node: Type[DoubleLinkedNode]) -> None:
        """
        Setter for tail node, validates correct type

        Args:
            new_node (DoubleLinkedNode): New node which will be tail_node

        Raises:
            TypeError: this is raised if new_node is not a DoubleLinkedNode
        """
        if (isinstance(new_node, DoubleLinkedNode)
                or new_node is None):
            self._tail_node = new_node
        else:
            raise TypeError(
                f"new node: {str(new_node)} is not a compatible Node")

    def add_to_head(self, new_node_value: Any) -> None:
        """
        Creates a new head node containing this value,
        updates the new head node to be linked to the old head node.

        Args:
            new_node_value (Any): create a new node with this value
        """
        # create a new node with this value
        new_node = DoubleLinkedNode(
            value=new_node_value, next_node=self.head_node)
        self.head_node.prev_node = new_node
        self.head_node = new_node

    def remove_node(self, value_to_remove: Any) -> None:
        """
        Remove all nodes with this value.

        Args:
            value_to_remove (Any): [description]
        """

        # start at the head
        current_node = self.head_node
        # if the head is to be removed
        # remove
        if current_node.value == value_to_remove:
            self.head_node = current_node.next_node
        else:
            while current_node:  # is not None (a)
                # look at the next node (b)
                next_node: Optional[Type[DoubleLinkedNode]
                                    ] = current_node.next_node
                # if it matches the value to remove and is not none
                if next_node and next_node.value == value_to_remove:
                    # change nodes from a > b > c
                    # to a > c
                    current_node.next_node = next_node.next_node
                    next_node.next_node.prev_node = current_node
                    # then start the check from c
                    current_node = next_node.next_node
                else:
                    if next_node is None:
                        self.tail_node = current_node
                    current_node = next_node

    def swap_nodes(self, val1: Any, val2: Any) -> None:
        """
        Swap two nodes based on value
        returns none. Logs are made if this fails

        Args:
            val1 (Any): value of node to swap
            val2 (Any): second value of node to swap
        """

        # Two pointer solution.
        node1_prev: Optional[DoubleLinkedNode] = None
        node2_prev: Optional[DoubleLinkedNode] = None
        node2_next: Optional[DoubleLinkedNode] = None
        node1_next: Optional[DoubleLinkedNode] = None
        node1: Optional[DoubleLinkedNode] = self.head_node
        node2: Optional[DoubleLinkedNode] = self.head_node

        # stop
        if val1 == val2:
            logger.info("Elements are the same - no swap needed")
            return

        # iterate though and find node to swap
        while node1 is not None:
            if node1.value == val1:
                break
            # move along the list - find previous and next to use for swap
            node1_prev = node1
            node1_next = node1.next_node.next_node
            node1 = node1.next_node

        while node2 is not None:
            if node2.value == val2:
                break
            node2_prev = node2
            node2_next = node2.next_node.next_node
            node2 = node2.next_node

        if (node1 is None or node2 is None):
            logger.info(
                "Swap not possible - one or more element is not in the list")
            return

        if node1_prev is None:
            # there is no previous node therefore node1 was head
            # so set node2 as head
            self.head_node = node2
        else:
            node1_prev.next_node = node2

        if node1_next is None:
            # then node1 was the tail
            self.tail_node = node2
        else:
            # point backwards at node2
            # and forward to next node
            node1_next.prev_node = node2

        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.next_node = node1

        if node2_next is None:
            # then node2 was the tail
            self.tail_node = node1
        else:
            node2_next.prev_node = node1
        

        # create a temp node otherwise becomes infinite loop!
        temp = node1.next_node
        node1.next_node = node2.next_node
        node2.next_node = temp

        temp2 = node1.prev_node
        node2.prev_node = node2.prev_node
        node2.prev_node = temp2

        return

    def __str__(self) -> str:
        """
        Creates String represenation of the class.
        time - O(n) - O(2n) - calls superclass and then iterates again.
        space - O(1) - Some objects created however should be < n

        Returns:
            str: [description]
        """
        # call superclass
        string: str = super().__str__()
        string += "(t)"

        inserts_i: List[int] = []
        for index, char in enumerate(string):
            if char == "-" and string[index+1] == "-":
                inserts_i.append(index)
        for i in reversed(inserts_i):
            string = string[:i] + "p<" + string[i:]

        return string

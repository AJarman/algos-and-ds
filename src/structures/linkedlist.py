"""Linked List implementations"""
from logging import getLogger
from typing import Any, Optional, Type

from .nodes import SinglyLinkedNode

logger = getLogger(__name__)


class LinkedList:
    """
    Python Implementation of a singly linked list
    """

    def __init__(self, head_value: Any) -> None:
        """
        Constructor for Linkedlist, add a head value
        time - O(1) - constant time
        space - O(1) - single object created inside function.

        Args:
            head_value (Any): value of any type to be the head
        """
        self.head_node = SinglyLinkedNode(head_value)

    @property
    def head_node(self) -> Type[SinglyLinkedNode]:
        """
        Getter for head_node
        time - O(1) - constant time
        space - O(0) - no space required

        Returns:
            Type[SinglyLinkedNode]: the head node
        """
        return self._head_node

    @head_node.setter
    def head_node(self, new_node: Type[SinglyLinkedNode]) -> None:
        """
        Setter for head node, validates correct type
        time - O(1) - constant time
        space - O(1) - constant space. Only new_node created

        Args:
            new_node (SinglyLinkedNode): New node which will be head_node

        Raises:
            TypeError: this is raised if new_node is not a SinglyLinkedNode
        """
        if (isinstance(new_node, SinglyLinkedNode)
            or new_node is None
                or issubclass(new_node, SinglyLinkedNode)):
            self._head_node = new_node
        else:
            raise TypeError(
                f"new node: {str(new_node)} is not a compatible Node")

    def __len__(self) -> int:
        """
        Calculates number of nodes
        time - O(n) - Linear time with length of list
        space - O(1) from O(2) - Constant space with 2 extra variables

        Returns:
            int: number of nodes
        """
        length = 0
        current_node = self.head_node
        while current_node:
            length += 1
            current_node = current_node.next_node

        return length

    def __str__(self) -> str:
        """ String representation
        head is marked with (h)
        next node is denoted with -->n
        time - O(n) - Linear time
        space - O(n) - string will get bigger with list size.

        Returns:
            str: [description]
        """
        string: str = ""
        node_index = 0
        current_node: Type[SinglyLinkedNode] = self.head_node
        while current_node:
            if node_index == 0:
                tag = "(h)"
            else:
                tag = "-->n"
            string += f"{tag}[{node_index}]:{str(current_node.value)}"
            current_node = current_node.next_node
            node_index += 1

        return string

    def __repr__(self) -> str:
        """returns __str__
        - time - see __str__
        - space - see __str__

        Returns:
            str: output from __str__
        """
        return self.__str__()

    def __iter__(self) -> Optional[Type[SinglyLinkedNode]]:
        """Allows iteration
        - time - O(1) - as just calling self.next
        - space - O(1) - only creating 'current'

        Returns:
            Optional[Type[SinglyLinkedNode]]: yielded when iterating

        Yields:
            Iterator[Optional[Type[SinglyLinkedNode]]]: iteration of the object.
        """

        current = self.head_node
        while current:
            yield current
            current = current.next_node

    def __getitem__(self, index: int) -> Type[SinglyLinkedNode]:
        """Implements indexing the linkedlist
        - time - O(n) - iterates through list in linear fashion
        - space - O(1) - O(3) - 3 variables created

        Args:
            index (int): index where value could be found

        Raises:
            IndexError: when index out of range

        Returns:
            Any: value at the given index.
        """

        while index < 0:
            # Index is a negative, so addition will subtract.
            index += len(self)
        if index >= len(self):
            raise IndexError(f"Index of {index} is out of "
                             f"range for {self.__class__.__name__} of length {len(self)}")

        current_index: int = 0
        current = self.head_node
        while current:
            if index == current_index:
                return current
            current_index += 1
            current = current.next_node

    def __contains__(self, value: Any) -> bool:
        """Implements the 'in' keyword
        time - O(n) - Linear time iterates through list
        space - O(1) - creates one variable 'i'


        Args:
            value (Any): Value to be found in the linkedlist

        Returns:
            bool: whether value found.
        """
        for i in self:
            if i.value == value:
                return True
        return False

    def add_to_head(self, new_node_value: Any) -> None:
        """
        Creates a new head node containing this value,
        updates the new head node to be linked to the old head node.
        time - O(1) - Constant time
        space - O(1) - Constant space, max one object created.

        Args:
            new_node_value (Any): create a new node with this value
        """
        # create a new node with this value
        new_node = SinglyLinkedNode(
            value=new_node_value, next_node=self.head_node)
        self.head_node = new_node

    def remove_node(self, value_to_remove: Any) -> None:
        """
        Remove all nodes with this value.
        time - O(n) - linear time with size of list in while loop
        space - O(1) - only current_node added

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
                next_node: Optional[Type[SinglyLinkedNode]
                                    ] = current_node.next_node
                # if it matches the value to remove and is not none
                if next_node and next_node.value == value_to_remove:
                    # change nodes from a > b > c
                    # to a > c
                    current_node.next_node = next_node.next_node
                    # then start the check from c
                    current_node = next_node.next_node
                else:
                    current_node = next_node

    def swap_nodes(self, val1: Any, val2: Any) -> None:
        """Swap two nodes based on value
        returns none. Logs are made if this fails
        time -  O(n) - from O(2n) - Linear time two iterations of list of n.
        space - O(1) - from O(4) - 5 extra variables created.
        Args:
            val1 (Any): value of node to swap
            val2 (Any): second value of node to swap
        """

        # Two pointer solution.
        node1_prev = None
        node2_prev = None
        node1 = self.head_node
        node2 = self.head_node

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
            node1 = node1.next_node

        while node2 is not None:
            if node2.value == val2:
                break
            node2_prev = node2
            node2 = node2.next_node

        if (node1 is None or node2 is None):
            logger.info(
                "Swap not possible - one or more element is not in the list")
            return

        if node1_prev is None:
            # there is no previous node therefore node1 was head
            self.head_node = node2
        else:
            # the previous node
            node1_prev.next_node = node2

        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.next_node = node1

        # create a temp node
        temp = node1.next_node
        node1.next_node = node2.next_node
        node2.next_node = temp

    def get_nth_last_node(self, n_nodes:int)->Optional[Type[SinglyLinkedNode]]:
        """Originally on Codecademy 
        
        Return
        time - O(n) - Linear time, one loop two pointers
        space - O(1) - Constant space as using two pointers.

        Args:
            n_nodes (int): number of nodes from tail

        Returns:
            Optional[Type[SinglyLinkedNode]]: returns node object if
        n < length of list. Otherwise returns None.
        """
        current = None
        tail_seeker = self.head_node
        count = 0
        while tail_seeker:
            tail_seeker = tail_seeker.next_node
            count += 1
            if count >= n_nodes:
                if current is None:
                    current = self.head_node
                else:
                    current = current.get_next_node()
        return current
    
    @property
    def middle_node(self)->Type[SinglyLinkedNode]:
        """Originally on Codecademy
        Using Two pointer approach, find middle node.
        time - O(n) - Linear time
        space - O(1) - Two Variables

        Returns:
            Type[SinglyLinkedNode]: The middle Node
        """
        fast = self.head_node
        slow = self.head_node
        while fast:
            fast = fast.next_node
            if fast:
                fast = fast.next_node
                slow = slow.next_node
        return slow

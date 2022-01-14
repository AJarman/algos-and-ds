"""Node Data structures"""
from typing import Any, Optional, Type


class SinglyLinkedNode:
    """
    Singly linked Node
    """

    def __init__(self, value: Any, next_node: Optional[Type["SinglyLinkedNode"]] = None):

        self.value: Any = value
        self.next_node: Optional[Type["SinglyLinkedNode"]] = next_node

    @property
    def next_node(self) -> Optional[Type["SinglyLinkedNode"]]:
        """returns linked node

        Returns:
            Node or None : Will return the Node if one linked
        """
        return self._next_node

    @next_node.setter
    def next_node(self, node: Type["SinglyLinkedNode"]) -> None:
        """Set the next node variable, will type check the next_node

        Args:
            node (Type[SinglyLinkedNode]): same as this class
            or subclass of this class.

        Raises:
            TypeError: will raise an error if invalid class.
        """

        if isinstance(node, self.__class__) or node is None:
            # check if this is the same as this class
            # (inherited in subclasses)
            self._next_node = node
        else:
            raise TypeError(
                f"new node: {str(node)} is not a compatible Node")

    @property
    def value(self) -> Any:
        """Get the node value

        Returns:
            Any : value of the Node
        """
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        """ Setter for the value

        Args:
            value (Any): any value that will be this nodes' data
        """
        self._value = value

    def __str__(self) -> str:
        """
        Node representation as a string, uses superclass

        Returns:
            str: Value and Next nodes' value
        """
        string: str = f"Value: \'{str(self.value)}\', Next Node: "
        if self.next_node:
            string += f"\'{str(self.next_node.value)}\'"
        else:
            string += "None"

        return string


    def __repr__(self):
        return f"<Instance of {self.__class__.__name__} class, {self.__str__()}>"


class DoubleLinkedNode(SinglyLinkedNode):
    """
    Doubly linked Node
    """

    def __init__(
        self,
        value: Any,
        next_node: Optional[Type["SinglyLinkedNode"]] = None,
        prev_node: Optional["DoubleLinkedNode"] = None,
    ) -> None:
        """Constructor of Doubly linked node

        Args:
            value (Any): [description]
            next_node (Optional[Type[, optional): [description]. Defaults to None.
            prev_node (Optional[, optional): [description]. Defaults to None.
        """

        super().__init__(
            value=value, next_node=next_node)
        self.prev_node = prev_node

    @property
    def prev_node(self) -> Type["DoubleLinkedNode"]:
        """returns linked node

        Returns:
            Node or None : Will return the Node if one linked
        """
        return self._prev_node

    @prev_node.setter
    def prev_node(self, node: Optional[Type["DoubleLinkedNode"]]) -> None:
        """Set the link node variable

        Args:
            node, Type["DoubleLinkedNode"]: node to be linked
        """

        if isinstance(node, self.__class__) or node is None:
            # check if this is the same as this class
            # (inherited in subclasses)
            self._prev_node = node
        else:
            raise TypeError(
                f"new node: {str(node)} is not a compatible Node")

    def __str__(self) -> str:
        """
        Node representation as a string, uses superclass

        Returns:
            str: Value of node, next node and previous node.
        """
        string: str = f"{super().__str__()}, Previous Node: "
        if self.prev_node:
            string += f"\'{str(self.prev_node.value)}\' "
        else:
            string += "None"

        return string

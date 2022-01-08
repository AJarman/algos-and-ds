"""Node Data structures"""
from typing import Any, Optional, Type


class SinglyLinkedNode:
    """
    Singly linked Node
    """

    def __init__(self, value: Any, next_node: Optional[Type["SingleLinkNode"]] = None):
        self._value = value
        self._next_node = next_node

    @property
    def next_node(self) -> Type["SingleLinkNode"]:
        """returns linked node

        Returns:
            Node or None : Will return the Node if one linked
        """
        return self._next_node

    @next_node.setter
    def next_node(self, node: Type["SingleLinkNode"]) -> None:
        """Set the next node variable, will type check the next_node

        Args:
            node (Type[SingleLinkNode]): same as this class
            or subclass of this class.

        Raises:
            TypeError: will raise an error if invalid class.
        """
        # """Set the link node variable

        # Args:
        #     next_node, Type["SingleLinkNode"]: node to be linked
        # """


        if isinstance(node, self.__class__):
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
        """Set the value of this Node

        Returns:
            None
        """
        self._value = value


class DoubleLinkedNode(SinglyLinkedNode):
    """
    Doubly linked Node
    """

    def __init__(
        self,
        value: Any,
        next_node: Optional[Type["SingleLinkNode"]] = None,
        prev_node: Optional["DoubleLinkedNode"] = None,
    ) -> None:
        """Constructor of Doubly linked node

        Args:
            value (Any): [description]
            next_node (Optional[Type[, optional): [description]. Defaults to None.
            prev_node (Optional[, optional): [description]. Defaults to None.
        """

        super(DoubleLinkedNode, self).__init__(
            value=value, next_node=next_node)
        self._prev_node = prev_node

    @property
    def prev_node(self) -> Type["DoubleLinkedNode"]:
        """returns linked node

        Returns:
            Node or None : Will return the Node if one linked
        """
        return self._prev_node

    @prev_node.setter
    def prev_node(self, node: Type["DoubleLinkedNode"]) -> None:
        """Set the link node variable

        Args:
            node, Type["SingleLinkNode"]: node to be linked
        """

        if isinstance(node, self.__class__):
            # check if this is the same as this class 
            # (inherited in subclasses)
            self._prev_node = node
        else:
            raise TypeError(
                f"new node: {str(node)} is not a compatible Node")

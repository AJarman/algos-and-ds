"""Node Data structures"""
from typing import Any, Optional, Type


class SingleLinkNode:
    """
    Singly linked Node
    """

    def __init__(self, value: Any, next_node: Optional[Type["SingleLinkNode"]] = None):
        self.value = value
        self.next_node = next_node

    def get_next_node(self) -> Type["SingleLinkNode"]:
        """returns linked node

        Returns:
            Node or None : Will return the Node if one linked
        """
        return self.next_node

    def set_next_node(self, next_node: Type["SingleLinkNode"]) -> None:
        """Set the link node variable

        Args:
            next_node, Type["SingleLinkNode"]: node to be linked
        """

        self.next_node = next_node

    def get_value(self) -> Any:
        """Get the node value

        Returns:
            Any : value within the node
        """
        return self.value

    def set_value(self, value: Any) -> None:
        """Set the value of this Node

        Returns:
            None
        """
        self.value = value


class DoubleLinkedNode(SingleLinkNode):
    """Doubly linked Node"""

    def __init__(
        self,
        value: Any,
        next_node: Optional[Type["SingleLinkNode"]] = None,
        prev_node: Optional["DoubleLinkedNode"] = None,
    ) -> None:

        super(DoubleLinkedNode, self).__init__(value=value, next_node=next_node)
        self.prev_node = prev_node

    def get_prev_node(self) -> Type["SingleLinkNode"]:
        """returns linked node

        Returns:
            Node or None : Will return the Node if one linked
        """
        return self.prev_node

    def set_prev_node(self, node: Type["SingleLinkNode"]) -> None:
        """Set the link node variable

        Args:
            node, Type["SingleLinkNode"]: node to be linked
        """

        self.prev_node = node

#!/usr/bin/python3
"""
Module that defines a Node and a SinglyLinkedList class.
"""

class Node:
    """
    A class that defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new node.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node in the list. Defaults to None.

        Raises:
            TypeError: If data is not an integer or if next_node is not a Node object or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
            int: The current data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Args:
            value (int): The new data of the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the list.

        Returns:
            Node or None: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node of the current node.

        Args:
            value (Node or None): The new next node.

        Raises:
            TypeError: If next_node is not a Node object or None.
        """
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new empty singly linked list.
        """
        self.__head = None

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string with all node data, each on a new line.
        """
        current = self.__head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < new_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

#!/usr/bin/python3
"""
Module for python singly linked list
"""


class Node:
    """Node class for a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialization method with data and optional next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data."""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class for a singly linked list."""

    def __init__(self):
        """Initialization method for an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list."""
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None
            and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """String representation of the entire list."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()


# Test case
if __name__ == "__main__":
    SinglyLinkedList = SinglyLinkedList()

    values_to_insert = [2, 5, 3, 10, 1, -4, -3, 4, 5, 12, 3]

    for value in values_to_insert:
        SinglyLinkedList.sorted_insert(value)

    print(SinglyLinkedList)

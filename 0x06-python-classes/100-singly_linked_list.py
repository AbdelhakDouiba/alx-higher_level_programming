#!/usr/bin/python3
"""
Node class
"""


class Node:
    """Node that defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Define Node with attributes

            Args:
                data: data to be hold
                next_node: next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, data):
        """data setter"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = data

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list"""
    def __init__(self):
        """Initialize the SinglyLinkedList class with attributes

            Args:

                head: the head of the singly linked list
        """
        self.__head = None

    def __str__(self):
        """The printable string of the class"""
        return_str = ""
        current_Node = self.__head
        while current_Node is not None:
            return_str += str(current_Node.data)
            current_Node = current_Node.next_node
            if current_Node is not None:
                return_str += "\n"
        return return_str

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list"""
        new_node = Node(value)
        tmp = self.__head
        if self.__head is None:
            self.__head = new_node
        elif tmp.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

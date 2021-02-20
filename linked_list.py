class LinkedList:

    """
    initializes attributes size, head, tail
    """
    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None
    """
    add(): adds item x to the end of the linked list:
        creates an object of Node() called p
        stores x in the data attribute of Node p
        creates a link from the next attribute of Node p to Node head
        if the list is empty, sets Node tail to be Node p
        sets Node head to Node p
        increments size of list by 1
    """
    def add(self, x):
        p = Node()
        p.set_data(x)
        p.set_next(self.__head)
        if self.__head is None:
            self.__tail = p
        self.__head = p
        self.__size += 1
        return True

    """
    remove(): removes the item from either the front or back of the list 
    depending on if it's a stack or queue:
        when i = 0 and i != size - 1 (removing from the front of the list):
            sets Node head to the next node of Node head
            if the next node of Node head didn't exist, set Node tail to None
        when i = size - 1 (removing from the rear of the list):
            assigns Node tail to variable p
            assigns Node head to to variable q
            loops until Node q is the second to last node in the list
            sets Node tail to be the second to last node
            deletes the next node of tail by setting it to None
        decrements size of list by one
        returns the data attribute of the node that was just dequeued
    """
    def remove(self, i):
        if i == 0:
            removed = self.__head.get_data()
            self.__head = self.__head.get_next()
            if self.__head is None:
                self.__tail = None
        elif i == self.__size - 1:
            removed = self.__tail.get_data()
            q = self.__head
            pos = 0
            while pos < i - 1:
                q = q.get_next()
                pos += 1
            if self.__tail is not self.__head:
                self.__tail = q
            self.__tail.set_next(None)
        else:
            removed = self.__head.get_data()
            self.__head = self.__head.get_next()
            if self.__head is None:
                self.__tail = None
        self.__size -= 1
        return removed

    # setters and getters
    def set_head(self, head):
        self.__head = head

    def set_tail(self, tail):
        self.__tail = tail

    def set_size(self, size):
        self.__size = size

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def get_size(self):
        return self.__size


class Node:

    """
    initializes attributes prev, next, and data
    """
    def __init__(self):
        self.__prev = None
        self.__next = None
        self.__data = None

    # setter and getters
    def set_next(self, next):
        self.__next = next

    def set_prev(self, prev):
        self.__prev = prev

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

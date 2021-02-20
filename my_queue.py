import linked_list

class Queue(object):

    """
    initializes attribute linkedlist to be an object of LinkedList()
    initializes attribute front to -1
    initializes attribute rear to -1
    """
    def __init__(self):
        self.__linkedList = linked_list.LinkedList()
        self.__front = -1
        self.__rear = -1

    """
    enqueue(): adds item to rear of queue
        gets x from is_balanced()
        calls add(x) using linkedlist object
        increments rear by 1
    """
    def enqueue(self, x):
        self.__linkedList.add(x)
        self.__rear += 1

    """
    dequeue(): removes item from front of queue
        calls remove(top) using linkedlist object
        increments top by 1
        returns the item from the front of queue
    """
    def dequeue(self):
        dequeued = self.__linkedList.remove(self.__front)
        self.__front += 1
        return dequeued

    """
    is_empty(): returns Boolean of whether queue is currently empty
    """
    def is_empty(self):
        if self.__linkedList.get_head() is None:
            return True
        return False

    """
    clear(): clears the stack by reinitializing attributes
    """
    def clear(self):
        self.__linkedList = linked_list.LinkedList()
        self.__front = -1
        self.__rear = -1


class QueueParenthesesChecker(object):

    """
    initializes attribute queue1 to be an object of Queue()
    initializes attribute queue2 to be an object of Queue()
    """
    def __init__(self):
        self.__queue1 = Queue()
        self.__queue2 = Queue()

    """
    is_balanced(): checks if string s has balanced parentheses
        iterates through string
        if character is '(':
            if queue1 is empty, enqueues character
            if queue1 isn't empty:
                dequeues items from queue1 to queue2
                enqueues character to queue1
                dequeues items from queue2 to queue1
        if character is ')':
                if queue1 is empty, parentheses are not balanced
                if queue1 isn't empty, dequeue() is called
        after iterations, if queue1 is empty, parentheses are balanced
        if queue1 isn't empty, then parentheses aren't balanced
        clears/resets queue1
    """
    def is_balanced(self, s):
        for ch in s:
            if ch == '(':
                if self.__queue1.is_empty():
                    self.__queue1.enqueue(ch)
                else:
                    while self.__queue1.is_empty() is False:
                        self.__queue2.enqueue(self.__queue1.dequeue())
                    self.__queue1.enqueue(ch)
                    while self.__queue2.is_empty() is False:
                        self.__queue1.enqueue(self.__queue2.dequeue())
            elif ch == ')':
                if self.__queue1.is_empty():
                    return False
                else:
                    self.__queue1.dequeue()
        if self.__queue1.is_empty():
            return True
        self.__queue1.clear()
        return False

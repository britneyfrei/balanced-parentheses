import linked_list

class Stack(object):

    """
    initializes attribute linkedlist to be an object of LinkedList()
    initializes top to -1
    """
    def __init__(self):
        self.__linkedList = linked_list.LinkedList()
        self.__top = -1

    """
    push(): pushes item x onto stack
        gets x from is_balanced()
        calls add(x) using linkedlist object
        increments top by 1
    """
    def push(self, x):
        self.__linkedList.add(x)
        self.__top += 1

    """
    pop(): pops item from top of stack
        calls remove(top) using linkedlist object
        decrements top by 1
        returns the item from the top of the stack
    """
    def pop(self):
        popped = self.__linkedList.remove(self.__top)
        self.__top -= 1
        return popped

    """
    is_empty(): returns Boolean of whether stack is currently empty
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
        self.__top = -1


class StackParenthesesChecker(object):

    """
    initializes attribute stack to be an object of Stack()
    """
    def __init__(self):
        self.__stack = Stack()

    """
    is_balanced(): checks if string s has balanced parenthesis
        iterates through string
            if character is '(', pushes character
            if character is ')':
                if the stack is empty, parentheses are not balanced
                if stack isn't empty, pop() is called
        after iterations, if stack is empty, parentheses are balanced
        if stack isn't empty, then parentheses aren't balanced
        clears/resets the stack
    """
    def is_balanced(self, s):
        for ch in s:
            if ch == '(':
                self.__stack.push(ch)
            elif ch == ')':
                if self.__stack.is_empty():
                    return False
                else:
                    self.__stack.pop()
        if self.__stack.is_empty():
            return True
        self.__stack.clear()
        return False

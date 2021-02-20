import linked_list
import my_stack
import my_queue

"""
creates objects of StackParenthesesChecker() called checker1 and checker2
creates objects of Stack() and Queue() called stack, queue1, and queue2
loops until user doesn't want to continue
gets input from user and uses checkers to call is_balanced()
depending on if is_balanced() returns True or False, displays result
"""
def main():
    checker1 = my_stack.StackParenthesesChecker()
    checker2 = my_queue.QueueParenthesesChecker()
    stack = my_stack.Stack()
    queue1 = my_queue.Queue()
    queue2 = my_queue.Queue()
    setattr(stack, '_Stack__linkedList', linked_list.LinkedList())
    setattr(queue1, '_Queue__linkedList', linked_list.LinkedList())
    setattr(queue2, '_Queue__linkedList', linked_list.LinkedList())
    cont = 'Y'
    while cont == 'Y':
        user_str = input("Enter a string of parentheses: ")
        setattr(checker1, '_Stack__stack', my_stack.Stack())
        setattr(checker2, '_Queue__queue1', my_queue.Queue())
        setattr(checker2, '_Queue__queue2', my_queue.Queue())
        if checker1.is_balanced(user_str) and checker2.is_balanced(user_str):
            print('The input string', user_str, 'has balanced parentheses.')
        else:
            print('The input string', user_str,
                  'does not have balanced parentheses.')
        cont = input('Would you like to enter another string (Y or N)? ')


if __name__ == "__main__":
    main()

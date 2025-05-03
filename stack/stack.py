# creating a stack using a linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def pop(self):
        popped_node = self.head
        self.head = None if not self.head else self.head.next
        return popped_node

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def peek(self):
        return None if not self.head else self.head.val

    def isEmpty(self):
        return True if self.head else False
    
if __name__ == "__main__":
    stack = Stack()
    print(stack.peek())
    stack.push(7)
    print("The top of the stack is:", stack.peek())
    stack.push(6)
    print("The top of the stack is:", stack.peek())
    stack.pop()
    print("The top of the stack is:", stack.peek())
    stack.pop()
    print("The top of the stack is:", stack.peek())
    


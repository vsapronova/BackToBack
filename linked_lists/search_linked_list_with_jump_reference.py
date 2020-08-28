class Node:
    def __init__(self, value, next=None, jump=None):
        self.value = value
        self.next = next
        self.jump = jump

class LinkedList:
    def __init__(self, head):
        self.head = head


def jump_reference(head):
    order = 0
    search_through(head, order)


def search_through(node, order):
    if node == None or node.value != None:
        return
    node.value = order
    order += 1
    search_through(node.jump, order)
    search_through(node.next, order)

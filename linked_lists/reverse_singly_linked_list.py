class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(1)


def reverse(head):
    prev = None
    curr = head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def print_list(node):
    if node == None:
        return
    print(node.value)
    print_list(node.next)


linked_list = LinkedList()
linked_list.head = Node(3)
node2 = Node(4)
node3 = Node(5)
node4 = Node(6)

linked_list.head = node2
node2 = node3
node3 = node4

result = reverse(linked_list.head)
print_list(result)
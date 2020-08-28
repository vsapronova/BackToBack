class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Linked_List:
    def __init__(self, head):
        self.head = head


def check_overlap(l1, l2):
    seen = set()
    curr = l1
    while curr != None:
        seen.add(curr)
        curr = curr.next
    curr2 = l2
    while curr2 != 0:
        if curr2 in seen:
            return print(curr2.value)
        curr2 = curr2.next
    return None


l1 = Linked_List(Node(1, Node(2, Node(3, Node(4, Node(5))))))
l2 = Linked_List(Node(4, Node(0, Node(3, Node(4, Node(5))))))

check_overlap(l1, l2)



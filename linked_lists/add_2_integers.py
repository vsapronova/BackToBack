class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head



def add_int(l1, l2):
    carry = 0
    cur1 = l1
    cur2 = l2
    dummy_head = Node(0)
    cur3 = dummy_head
    while cur1 != None or cur2 != None:
        first = cur1.value if cur1 != None else 0
        second = cur2.value if cur2 != None else 0

        new_sum = first + second + carry
        carry = new_sum//10

        cur3.next = Node(new_sum % 10)

        if cur1 != None:
            cur1 = cur1.next
        if cur2 != None:
            cur2 = cur2.next

        cur3 = cur3.next
    if carry > 0:
        cur3.next = Node(carry)
    return dummy_head.next

l1 = LinkedList(Node(2, Node(3, Node(4))))
l2 = LinkedList(Node(1, Node(5, Node(7))))

print(add_int(l1, l2))


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str(self, seen=[]):
        if self in seen:
            return str(self.value) + " -> ...!"
        seen.append(self)
        if not self.next is None:
            return str(self.value) + " -> " + self.next.__str(seen)
        return str(self.value)

    def __str__(self):
        return self.__str()

class Linked_List:
    def __init__(self, head):
        self.head = head


def swap_pairs(head):
    if head == None or head.next == None:
        return head
    first = head
    second = head.next

    head = head.next
    while True:
        start_second_pair = second.next
        second.next = first
        if start_second_pair == None or start_second_pair.next == None:
            first.next = start_second_pair
            return head
        first.next = start_second_pair.next
        first = start_second_pair
        second= start_second_pair.next


print(swap_pairs(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))))
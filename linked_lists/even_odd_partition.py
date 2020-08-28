class Node:
    def __init__(self, value, next = None):
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

    # first way
    def even_odd_partition(self):
        if self.head == None or self.head.next == None:
            return self.head
        curr = self.head
        dummy_even_head = Node(-1)
        dummy_even_tail = dummy_even_head
        dummy_odd_head = Node(-1)
        dummy_odd_tail = dummy_odd_head
        index = 0
        while curr != None:
            if index % 2 == 0:
                dummy_even_tail.next = curr
                dummy_even_tail = curr
            else:
                dummy_odd_tail.next = curr
                dummy_odd_tail = curr

            curr = curr.next
            index += 1
        dummy_even_tail.next = dummy_odd_head.next
        return dummy_even_head.next

    #second way
    def even_odd_partition2(self):
        if self.head == None or self.head.next == None:
            return self.head
        even = self.head
        odd = even.next
        odd_head = odd
        while odd != None and odd.next != None:
            even.next = odd.next
            even = odd.next
            odd.next = even.next
            odd = even.next
        even.next = odd_head
        return self.head


a = Linked_List(Node(0, Node(1, Node(2, Node(3, Node(4))))))
# print(a.even_odd_partition())
print(a.even_odd_partition2())
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

    def length(self):
        curr = self
        count = 0
        while curr != None:
            curr = curr.next
            count+=1
        return count

class Linked_List:
    def __init__(self, head):
        self.head = head

    def right_shift(self, k):
        if self.head == None:
            return self.head
        curr = self.head
        len_list = self.head.length()
        while curr.next != None:
            curr = curr.next
        old_tail = curr
        old_tail.next = self.head
        curr = self.head
        k = k%len_list
        if k == 0:
            return self.head
        n = len_list - k
        while n != 1:
            curr = curr.next
            n -= 1
        new_head = curr.next
        curr.next = None
        return new_head

a = Linked_List(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))))
print(a.right_shift(7))
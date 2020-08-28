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

    # brute force
    def remove_kth(self, k):
        if self.head == None or self.head.next == None:
            return self.head
        length_ll = self.head.length()
        new_len = length_ll - k
        curr = self.head
        prev = None
        if new_len < 1:
            return self.head.next
        else:
            while new_len != 0:
                prev = curr
                curr = curr.next
                new_len -= 1
            prev.next = curr.next
        return self.head

    def remove_kth2(self, k):
        if self.head == None or self.head.next == None:
            return self.head
        fast = self.head
        slow = self.head
        prev = None
        while k != 0:
            fast = fast.next
            k -= 1
        while fast != None:
            fast = fast.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return self.head










ll = Linked_List(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))))
# l2 = Linked_List(Node(1))
print(ll.remove_kth2(2))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
middle = find_middle_element(head)
print(middle.val) 

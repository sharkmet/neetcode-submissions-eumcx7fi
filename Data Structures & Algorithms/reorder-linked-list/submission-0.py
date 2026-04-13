# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None
        prev = None
        

        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        
        l1 = head
        l2 = prev

        while l1 and l2:
            after1 = l1.next
            after2 = l2.next
            l1.next = l2
            l2.next = after1
            l1 = after1
            l2 = after2


        
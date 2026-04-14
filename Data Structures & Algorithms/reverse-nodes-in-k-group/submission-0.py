# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        curr=head

        while curr:
            # check if k nodes remain
            check = curr
            for i in range(k):
                if not check:
                    return dummy.next  # fewer than k nodes, leave as is
                check = check.next
            
            # save next group head
            next_group_head = check

            # save tail before reversing
            group_tail = curr

            # reverse k nodes
            prev = None
            for i in range(k):
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
            # prev is now the new head, curr is next group head
 
            # reconnect
            prev_group_tail.next = prev
            group_tail.next = next_group_head
            prev_group_tail = group_tail

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next

        rmIdx = N - n
        if rmIdx == 0:
            return head.next

        curr = head
        for i in range(N - 1):
            if (i + 1) == rmIdx:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head
        
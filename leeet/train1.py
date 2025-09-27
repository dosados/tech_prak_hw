from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        carry = 0 
        while l1  or l2 or carry: 
            cur.val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, cur.val = divmod(cur.val, 10)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            if carry or l1 or l2:
                cur.next = ListNode()
                cur = cur.next

        return res
    

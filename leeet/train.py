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
        while l1 is not None and l2 is not None: 
            cur.val += l1.val
            cur.val += l2.val

            cur.next = ListNode()

            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            cur.val += l1.val
            cur.next = ListNode()
            cur = cur.next
            l1 = l1.next

        while l2 is not None:
            cur.val += l2.val
            cur.next = ListNode()
            cur = cur.next
            l2 = l2.next

        cur = res
        pred = res
        carry = 0
        while cur.next is not None:
            new_carry = (cur.val + carry) // 10
            cur.val = (carry + cur.val) % 10
            carry = new_carry
            pred = cur
            cur = cur.next

        cur.val = (carry + cur.val) % 10

        if cur.val == 0:
            pred.next = None
            

        return res
            

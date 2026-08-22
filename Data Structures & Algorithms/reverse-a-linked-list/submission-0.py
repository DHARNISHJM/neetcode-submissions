# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        curr = head # this denotes the node we will be working on
        prev = None # this denotes the node that will be next to the curr node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

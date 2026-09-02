# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def mergeTwoLinkedLists(self,list1, list2):
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next
            else:
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next

        dummy.next = list1 or list2

        return node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        while len(lists) > 1:
            merged = []

            for i in range(0,len(lists),2):
                if i+1 < len(lists):
                    merged.append(self.mergeTwoLinkedLists(lists[i], lists[i+1]))
                else:
                    merged.append(lists[i])

            lists = merged

        return lists[0]

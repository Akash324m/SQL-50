# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        arr = []
        for l in lists:
            while l:
                arr.append(l.val)
                l= l.next
        arr.sort()

        dummy= ListNode()
        current=dummy

        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

     
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            #fast and fast.next feels safer somehow
            #how many executions when 4 nodes?
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None

        prev = None
        while second:
            # i know for a fact the new head node is always prev here
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        second = prev 
        first = head
        while first and second:
            fnxt = first.next
            snxt= second.next
            first.next = second
            first = fnxt
            second.next = fnxt
            second = snxt
        
     

        


        

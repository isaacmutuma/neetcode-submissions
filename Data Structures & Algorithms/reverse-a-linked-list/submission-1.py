# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            #current forward
            nxt=curr.next
            #reversing current backward
            curr.next=prev
            #next iteration
            prev=curr
            curr=nxt
        return prev
        

        
        
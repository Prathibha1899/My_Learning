# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        lead=head
        lag=head
        count=0
        if head.next==None:
            return None
        while lead.next!=None:
            if count<n:
                lead=lead.next
                count=count+1
            else:
                lead=lead.next
                lag=lag.next
        if count==n-1:
            head=head.next
        else:
            lag.next=lag.next.next
        return head
        
        
        
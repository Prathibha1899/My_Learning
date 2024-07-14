"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        current_node=head
        previous=None
        next_node=None
        while current_node:
            next_node=current_node.next
            current_node.next=previous
            previous=current_node
            current_node=next_node
            head=previous
        return head
        
        
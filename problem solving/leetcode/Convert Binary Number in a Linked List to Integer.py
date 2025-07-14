# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary=0
        res=0
        current=head
        while current:
            binary=(binary*10)+current.val
            current=current.next
        power=0
        while binary:
            if binary%10==1:
                res+=2**power
            power+=1
            binary=binary//10
        
        return res

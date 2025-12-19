"""
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
"""

class Solution:
    def cycleStart(self, head):
        slow = head
        fast = head
        
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            
            if(slow == fast):
                slow = head
                while(slow != fast):
                    slow = slow.next
                    fast = fast.next
                return slow.data
        return -1
        
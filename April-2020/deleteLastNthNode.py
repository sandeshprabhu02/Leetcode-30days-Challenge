"""

Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, item):
        new_node = ListNode(item) 
        if self.head is None: 
            self.head = new_node 
            return
        last = self.head 
        while last.next: 
            last = last.next
        last.next = new_node
    
    def display(self): 
        temp = self.head 
        while temp: 
            print(temp.val)
            temp = temp.next
    
    def deleteNthFromEnd(self, k):
        first = self.head
        second = self.head
        count = 1
        while count <= k:
            second =  second.next
            count += 1
        if second is None:
            self.head.val = self.head.next.val
            self.head.next = self.head.next.next
            return
        while second.next is not None: 
            first = first.next
            second = second.next
        first.next = first.next.next





val = [1, 2, 3, 4, 5] 
k = 2
ll = LinkedList() 
for i in val: 
    ll.push(i)

print("Linked list before modification:"); 
ll.display() 
  
ll.deleteNthFromEnd(k) 
  
print("\nLinked list after modification:"); 
ll.display() 


# class Solution:
#     def removeNthFromEnd(self, head, n):
#         return


# print(Solution().removeNthFromEnd(head, 2))
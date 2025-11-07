# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initializa dummy placeholder node dummy
        # returning dummy.next will return the head of the merged result list
        # initialize a pointer tail that will be used to track the end of the merged list as we build it
        dummy = ListNode(-1) # arbitrary
        tail = dummy # our starting point is dummy, before we start building the result list

        while list1 and list2: # both not empty
            if list1.val <= list2.val: # we will choose list1.val to append to result
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2
        #tail.next = list1 or list2

        return dummy.next

        
       
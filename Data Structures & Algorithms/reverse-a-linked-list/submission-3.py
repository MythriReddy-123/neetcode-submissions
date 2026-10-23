# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        temp = head

        while head != None:
            l.append(head.val)
            head = head.next
        print(l)
        list = l[::-1]
        print(list)
        head = temp
        i = 0
        while  head != None:
            head.val = list[i]
            head = head.next
            i += 1
        head = temp

        return head
        
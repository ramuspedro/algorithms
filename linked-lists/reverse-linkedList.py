# Problem: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
from typing import Optional, Union

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     current = head
    #     temp = head
    #     temp2 = None
    #     while current != None:
    #         current = current.next
    #         temp.next = temp2
    #         temp2 = temp
    #         temp = current
    #     return temp2

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # current = head
        # temp = head
        # temp2 = None
        # while current != None:
        #     current = current.next
        #     temp.next = temp2
        #     temp2 = temp
        #     temp = current
        # return temp2
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead

    def reverse_list(self, head, prev = None):
        if head is None:
            return prev
        next = head.next
        head.next = prev
        return self.reverse_list(next, head)


solution = Solution()
data = [1,2,3,4,5]
# headList = solution.connectLinkedList(data)
# print(headList)
headList = ListNode()
firstNode = ListNode(1, headList)
secondNode = ListNode(2, firstNode)
thirdNode = ListNode(3, secondNode)
solution.printLinkedList(headList)
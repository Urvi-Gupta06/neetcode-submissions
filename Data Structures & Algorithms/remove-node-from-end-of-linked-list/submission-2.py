# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # reverse list
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        reversed_head = prev

        # remove nth node
        counter = 1
        curr = reversed_head
        prev_node = None

        while curr:
            if counter == n:

                if prev_node is None:
                    # removing first node
                    reversed_head = curr.next
                else:
                    prev_node.next = curr.next

                break

            counter += 1
            prev_node = curr
            curr = curr.next

        # reverse again
        current = reversed_head
        previous = None

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous


        
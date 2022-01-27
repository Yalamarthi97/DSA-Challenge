"""
There are 2 approaches..

1. Reverse the linked list and then delete the entry value of n from the front
    This method involes 2 steps
        A. Reverse the linked list takes o(m) where m is the size
        B. Traverse it till n ( node to be deleted ) and delete it 
        Time complexity is o(m) as we can ignore the time taken to traverse again and delete it

2. We will be taking advantage of a simple math formula
        [0:end] = [:n] + [n:]
        This just means that the whole list can be broken down into 2 halves
            a. one list of all values till n 
            b. values after n till end

        We have separate pointer which we use it to go through the for loop ( seemed better to use rather than a pass statement)
        Once we hit the condition, we switch over to incrementing the head pointer till the secondary pointer reaches the end
           Why is this needed?
           This helps to increment the head pointer to the node n+1 from the back 
           Then we can proceed to delete it and map the rest

        Have checks in place where if the list has only 1 node we are returning a empty one
        check 2 : If the n is the size of the list, we directly replace the head to the next node in the start


        P.S This is what i had on my way of thinking.. it might be right or might have loopholes in it.. If it has loopholes do let me know so that i can rectify the same


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=1
        size=0
        tempA=head
        tempB=head
        if not head.next:
            return None
        while tempA:
            size+=1
            if count  < n+2:
                tempA=tempA.next
            else:
                tempA=tempA.next
                head=head.next
            count+=1
        if size - n ==0:
            head=tempB.next
            return head
        else:
            head.next=head.next.next
            head=tempB
            return head
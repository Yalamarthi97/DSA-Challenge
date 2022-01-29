"""
This one was a bit more tricky than i expected it to be

I almost did the same method but it was very difficult without recursion as i needed a lot of pointers. So i ended up understanding on how to do it with recursion

First we are going to reverse the linked list without issues till we hit the value of k, This is where recursion comes into play!
    As soon as we hit the K value
    current node will be the kth node
    next will be k+1 and prev  will point to the k-1 node


Now just call reverse on the k+1 nodes and append the prev ( return ) to head.next

Why head.next? y returning prev will write a separate blog on this!! it is under construction 
"""


class Solution:
    def reverse(self,head, k):
        if not head:
            return None
        # Code here
        count=0
        prev= None
        curr = head
        nextn=None
        while curr and count<k:
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
            count+=1
        if nextn:
            head.next=self.reverse(nextn,k)
        
        return prev
    
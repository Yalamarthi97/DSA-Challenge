"""
This might be a bit tricky to understand at first glance.. but once understood it is too simple!
Before we begin rethink the linked list
    if the list is 1->2->3->4->5 it is not just this but
                    None -> 1 -> 2 -> 3 -> 4 -> 5 -> None

we are taking 3 additional nodes
    current , previous , nextnode

    At the start the previous and nextnodes are None, current will be pointing to head

    Example list => 1->2->3->4
    Changing the list to => None -> 1 -> 2 -> 3 -> 4 -> None

    Pass1:
    None -> 1 -> 2 -> 3 -> 4 -> None
    prev   cur
    next
                    nextnode=current.next

    None -> 1 -> 2 -> 3 -> 4 -> None
    prev   cur
                nxt    

                current.next=prev
    
    None <- 1 -> 2 -> 3 -> 4 -> None
    prev   cur
                nxt

                previous = current

    None <- 1 -> 2 -> 3 -> 4 -> None
           cur
           prev nxt

                current = nextnode
    
    None <- 1 -> 2 -> 3 -> 4 -> None
                cur
           prev nxt

    After this at the start of Pass 2 we would be incrementing the next pointer to the point to 3 using nextnode=current.next
    And the whole flow continues till the end
"""



class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        previous=None
        current=head
        nextnode=None
        while current:
            nextnode=current.next
            current.next=previous
            previous=current
            current=nextnode
            
            
        
            
        
        return previous
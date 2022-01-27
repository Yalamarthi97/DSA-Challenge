"""
The simple way without concerns for time complexity is to store the address of all the nodes in a list
Iterate over the other comparing the address,  
    If hit. return the node
    else continue till the end

This method obviously has drawbacks where the memory used will be o(size of list) and it will do unwanted processing incase the lists are huge and the intersection is 
near the ending!
"""

"""This method is o(m+n) and o(1) space.. why?
o(m+n) because even though we have 2 complete for loops to get the size of the lists it will be o(m) and o(n) [ addition ]
space is o(1) because we are not using anything to store the list addresses expect 2 constant variables

"""


"""Method Explanation: 
1. We get the sizes of the lists
2. Find the difference between the lengths ( assume it is d ) to find out how many places to move the bigger list so that they both start at the same point.
3. Move the bigger list d positions 
4. Compar every node till hit
    if hit return the value,
    else return none
"""

        sizeA=0
        sizeB=0
        tempA=headA
        tempB=headB
        while tempA:
            sizeA+=1
            tempA=tempA.next
        while tempB:
            sizeB+=1
            tempB=tempB.next
        
        to_move = abs(sizeA-sizeB)
        if sizeA>sizeB:
            for i in range(0,to_move):
                headA=headA.next
        elif sizeB>sizeA:
            for i in range(0,to_move):
                headB=headB.next
        else:
            for i in range(0,to_move):
                headA=headA.next
        
        while headA!=None and headB!=None:
            if headA == headB:
                return ListNode(headA.val)
            headA=headA.next
            headB=headB.next
        return None
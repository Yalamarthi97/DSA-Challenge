"""This is a fairly straight forward approach just iterate over the list and keep track of number of executions of the while loop
    Return the number of executions! 
"""


class Solution:
    
    def getCount(self, head_node):
        #code here
        count=0
        while head_node:
            count+=1
            head_node=head_node.next
        return count

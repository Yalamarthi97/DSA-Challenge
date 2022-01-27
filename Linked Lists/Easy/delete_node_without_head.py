
###
# This is the solution for the problem https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/

# Way of thinking 1:
#           1. Since deletion of linked list takes o(n) no matter what, traverse the whole linked list 
#           2. Have a variable keeping track of previous element
#           3. When at the node do:
#               prev->next == node->next
#               remove(node)
# 
#           This doesn't work as we don't have access to the head 
# 
# Way of thinking 2:
#           1. Just replace the current node with the next one
#               Replace the value of the node with the value of the next node
#               Bypass the next node and map it to the current one!
#     I know this might be a bit overwhelming so wrote a blog on explaining the same in detailed manner.. do check it out! -> < https://ysriharsha.medium.com/remove-a-node-in-linked-list-without-traversing-it-ad2967b689b6 >
# 
# ###

#Actual 2 line code
node.val=node.next.val
node.next=node.next.next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root:
#             return -1
        
#         # initialize a variable current so we can traverse the tree
#         current = root

#         while current:
#             if p.val < current.val and q.val < current.val: # both node values less than node.val
#                 current = current.left

#             elif p.val > current.val and q.val > current.val: # both node values less than node.val
#                 current = current.right
#             # remaining case: split point is either current node, or root
#             else:
#                 return current

# # time complexity = O(h)
# # space complexity = O(1)

# recursive
# A function is a standalone block of code (defined at the top level).
# A method is a function bound to an instance of a class — it automatically receives self as the first argument.
class Solution:
     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # base case
        if not root:
            return None # exp output: a root node
        # recursive case
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root



        
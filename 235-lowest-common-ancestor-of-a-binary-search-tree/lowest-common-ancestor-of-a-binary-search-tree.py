# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # begin at root
        # set current equal to root
        # begin traversing
        # if both p and q values are less than root, curr = curr.left
        # if both more, curr = curr.right
        # otherwise, either they are on diff subtrees or one is the parent/ ancestor of the other
        # therefore it will be the lca (first common point)
        current = root

        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else: # two possibilities
                return current
            
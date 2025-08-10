# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base cases: 
        # both trees empty -> trivially true
        # one of the children present in one tree ND NOT THE OTHER, false
        # node.values are different at each level of the tree, false
        # recursive case:
        # call function for the left and right subtrees.

        if not p and not q:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        # recursive case:
        return(self.isSameTree(p.left, q.left) 
            and self.isSameTree(p.right, q.right))


        
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # create ancestors set
        ancestors = set()

        # add p and its parents to the ancestors set
        while p:
            ancestors.add(p)
            p = p.parent

        # traverse upwards from q until we find one in the set
        while q:
            if q in ancestors:
                return q
            q = q.parent

        return None # shouldn't happen if both nodes in same tree
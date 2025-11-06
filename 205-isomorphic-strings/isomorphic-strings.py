class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # edge cases
        if len(s) != len(t):
            return False
        
        if len(s) == 0 and len(t) == 0:
            return True
        # stores
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1
        return True
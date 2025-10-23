class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # given two strings
        # begin at idx 0 for both
        # append first idx from 1st wed, then 1st from 2nd, as we move right
        # if at end of one, append remaining letters to its end
        i = 0
        j = 0
        result = []

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            i += 1
            result.append(word2[j])
            j += 1


        if i < len(word1):
            result.append(word1[i:])

        if j < len(word2):
            result.append(word2[j:])

        
        return "".join(result)
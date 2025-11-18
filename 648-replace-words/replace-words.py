class TrieNode:
    def __init__(self):
        self.children = {} # dict mapping ch -> TrieNode
        self.isEnd = False # marks that root finishes at this point

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # build Trie
        root = TrieNode()
        for word in dictionary:
            curr = root
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.isEnd = True

        # helper to store shortest root for one word
        def findRoot(word):
            curr = root
            prefix = "" # gathers chars successfully followed in trie
            for ch in word:
                if ch not in curr.children:
                    return word
                curr = curr.children[ch]
                prefix += ch
                if curr.isEnd:
                    return prefix
            return word
         # replace each word
        res = []
        for w in sentence.split():
            res.append(findRoot(w))
        return " ".join(res)



        
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # numerically balanced
        # number within 10^6 constraiants
        # therefore, 1.000,000 upper bound
        # meaning we can go until 6
        def is_beautiful(x):
            # convert x to a string
            # ints are not iterable
            s = str(x)
            counts = {} # to store each char and its frewuency

            for ch in s:
                # if num is 0, return False
                if ch == "0":
                    return False
                counts[ch] = counts.get(ch, 0) + 1

                # to determine if beautiful
            for char, freq in counts.items():
                if freq != int(char):
                    return False
            return True
        # incrementally search for next beautiful character
        num = n + 1
        while True:
            if is_beautiful(num):
                return num
            num += 1

        
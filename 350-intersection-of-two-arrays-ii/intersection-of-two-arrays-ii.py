from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # in Python, Counter is a built in class that acts like a dictionary where keys: the element, values: the frequency of the element

        # nums = [1, 2, 2, 1]
        # Counter(nums) = {1:2, 2:2}

        count1 = Counter(nums1)
        res = [] # to store result

        for num in nums2:
            if count1[num] > 0:
                res.append(num)
                count1[num] -= 1
        return res
        
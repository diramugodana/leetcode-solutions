class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # convert to sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)

        # find intersection and convert back to list
        return list(set1.intersection(set2))
        # or return list(set1 & set2)
        
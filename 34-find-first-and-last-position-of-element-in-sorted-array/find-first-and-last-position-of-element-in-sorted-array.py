class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # helper function for biased bst
        def binary_search(nums, target, left_bias):
            left , right = 0, len(nums) - 1

            i = -1 # to store index of latest match

            # begin traversal of list
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else: # nums[mid] == target
                    i = mid # i stores idx of latest match

                    if left_bias:
                        right = mid - 1
                    else:
                        left = mid + 1
            return i
        # edge case
        if not nums:
            return [-1, -1]

        first = binary_search(nums, target, True)
        last = binary_search(nums, target, False)

        return [first, last]
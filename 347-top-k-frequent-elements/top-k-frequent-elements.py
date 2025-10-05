class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # return k most frequent elements
        # if k = 2, return arr of size 2 
        # generate empty freq map
        # goal: populate with frequencies
        # in order to map top frequencies, we need to count all
        count_map = {}
        max_frequency = 0
        for num in nums:
            count_map[num] = 1 + count_map.get(num, 0)

        arr = []
        for num, cnt in count_map.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

            

        
           
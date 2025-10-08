class TimeMap:
    # set -> O(1), get -> O(log n)
    def __init__(self):
        #But why not use OOP-style attributes like self.key, self.value, self.timestamp?
        #Because that would only store one key, one value, and one timestamp 
        # doesn't store many values per key over time
        # init a dict to store list of key -> (timestamp, val)
        #self.store = defaultdict(list)
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        # if not empty
        self.keyStore[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return "" # not present
        # values[mid[0]] -> timestamp
        # values[mid[1]] -> value
        values = self.keyStore[key]
        left = 0
        right = len(values) - 1
        result = "" #returns empty if no value found

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return result
        

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append((timestamp, value))
        else:
            self.data[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        values = self.data[key]

        l, r = 0, len(values) - 1
        index_highest = -1

        while l <= r:
            mid = (l + r)//2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                index_highest = mid
                l = mid + 1
            else:
                r = mid - 1

        if index_highest == -1:
            return ""
        return values[index_highest][1]


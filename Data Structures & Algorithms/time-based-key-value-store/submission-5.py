class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map.get(key, [])
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        
        res = self.map[key]
        l, r = 0, len(res) - 1
        while l <= r:
            mid = (l+r)//2

            if res[mid][0] > timestamp:
                r = mid - 1
            elif res[mid][0] < timestamp:
                l = mid + 1
            else:
                return res[mid][1]
        return res[r][1] if res[r][0] < timestamp else ""

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key][timestamp] = value
        else:
            self.data[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        if timestamp in self.data[key]:
            return self.data[key][timestamp]
        
        highest_timestamp = -1
        for time in self.data[key].keys():
            if time <= timestamp:
                highest_timestamp = max(highest_timestamp, time)
        if highest_timestamp == -1:
            return ""


        return self.data[key][highest_timestamp]


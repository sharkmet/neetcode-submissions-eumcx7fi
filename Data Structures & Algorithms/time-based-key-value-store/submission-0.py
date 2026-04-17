class TimeMap:

    def __init__(self):
        self.keyvalue = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.keyvalue.get(key):
            self.keyvalue[key].append([value, timestamp])
        else:
            self.keyvalue[key] = [[value, timestamp]]

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyvalue:
            return ""
        
        result = ""
        l = 0
        r = len(self.keyvalue[key]) - 1

        while l <= r:
            mid = l + (r-l) // 2

            if self.keyvalue[key][mid][1] <= timestamp:
                result = self.keyvalue[key][mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return result
        

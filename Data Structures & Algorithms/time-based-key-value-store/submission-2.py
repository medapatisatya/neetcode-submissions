import bisect
class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timemap:
            self.timemap[key].append([value, timestamp])
        else:
            self.timemap[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap: return ""
        index = bisect.bisect_left(self.timemap[key], timestamp, key=lambda x: x[1])
        
        if index == len(self.timemap[key]):
            return self.timemap[key][-1][0]
        
        elif index == 0:
            if timestamp == self.timemap[key][0][1]:
                return self.timemap[key][0][0]
            else:
                return ""
        else:
            if timestamp == self.timemap[key][index][1]:
                return self.timemap[key][index][0]
            else:
                return self.timemap[key][index-1][0]
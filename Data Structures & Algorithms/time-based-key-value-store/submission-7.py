class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        data = self.timemap[key]
        l, r = 0, len(data)-1
        res = ""
        while l <= r:
            m = (l+r) // 2
            if data[m][1] <= timestamp:
                res = data[m][0]
                l = m + 1
            else: r = m - 1
        return res


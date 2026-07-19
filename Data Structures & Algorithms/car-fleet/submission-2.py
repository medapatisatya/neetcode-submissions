class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(list(zip(position, speed)))
        count, m, i = 1, (target - ps[-1][0]) / ps[-1][1], len(position) - 2

        while i >= 0:
            time = (target - ps[i][0]) / ps[i][1]
            if time > m:
                m = time
                count += 1
            i -= 1
        
        return count

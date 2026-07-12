class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        ps = sorted(list(zip(position, speed)))
        m, fleets = (target - ps[-1][0]) / ps[-1][1], 1

        for p in ps[-2::-1]:
            nm = (target - p[0]) / p[1]
            if nm > m:
                fleets += 1
                m = nm
        
        return fleets
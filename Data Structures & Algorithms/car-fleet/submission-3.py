class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(list(zip(position, speed)))
        l, st = 0, [0]
        for item in ps[::-1]:
            time = (target-item[0]) / item[1]
            if st and st[-1] < time: st.append(time)
        return len(st) - 1

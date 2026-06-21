class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for st in strs:
            s.append(str(len(st))+'#'+st)
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        i, length, strs = 0, 0, []
        while i < len(s):
            if s[i] == '#':
                i += 1
                strs.append(s[i:i+length])
                i = i + length
                length = 0
            else:
                length = length * 10 + int(s[i])
                i += 1
        return strs
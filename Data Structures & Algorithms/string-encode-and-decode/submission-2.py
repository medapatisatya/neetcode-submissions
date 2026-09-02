class Solution:

    def encode(self, strs: List[str]) -> str:
        len_strings = [str(len(s)) + ";" + s for s in strs]
        return "".join(len_strings)
    def decode(self, s: str) -> List[str]:
        strs, j, i = [], 0, 0
        while i < len(s):
            if s[i] == ';':
                ln = int(s[j:i])
                strs.append(s[i+1: i+1+ln])
                j = i + 1 + ln
                i = i + 1 + ln
            i += 1
        return strs
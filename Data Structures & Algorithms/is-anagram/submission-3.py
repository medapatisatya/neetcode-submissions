class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        # Using HashMap 
        # if not len(s) == len(t): return False

        # def counter(word):
        #     c = dict()
        #     for ch in word:
        #         c[ch] = 1 + c.get(ch, 0)
        #     return c
        
        # def compare(c1, c2):
        #     if not len(c1) == len(c2): return False

        #     for ch in c1:
        #         if not c1[ch] == c2.get(ch, 0): return False
        #     return True


        # scr, tcr = counter(s), counter(t)
        # return compare(scr, tcr) and compare(tcr, scr)

        # Fixed len of list approach
        if not len(s) == len(t): return False
        l = [0] * 26

        for i in range(len(s)):
            l[ord(s[i]) - ord('a')] += 1
            l[ord(t[i]) - ord('a')] -= 1

        for i in l:
            if i != 0: return False
        return True        
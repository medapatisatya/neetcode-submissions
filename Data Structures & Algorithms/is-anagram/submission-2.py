class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if not len(s) == len(t): return False

        def counter(word):
            c = dict()
            for ch in word:
                c[ch] = 1 + c.get(ch, 0)
            return c
        
        def compare(c1, c2):
            if not len(c1) == len(c2): return False

            for ch in c1:
                if not c1[ch] == c2.get(ch, 0): return False
            return True


        scr, tcr = counter(s), counter(t)
        return compare(scr, tcr) and compare(tcr, scr)
        
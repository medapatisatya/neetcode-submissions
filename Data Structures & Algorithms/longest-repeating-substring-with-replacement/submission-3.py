class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Brute Force
        # res = 0
        # for i in range(len(s)):
        #     count, maxf = {}, 0
        #     for j in range(i, len(s)):
        #         count[s[j]] = 1 + count.get(s[j], 0)
        #         maxf = max(maxf, count[s[j]])
        #         if (j - i + 1) - maxf <= k:
        #             res = max(res, j - i + 1)
        # return res

        #Optimized
        l, r, ml, mc, cl = 0, 0, 0, 0, defaultdict(int)
        while r < len(s):
            cl[s[r]] += 1
            
            mc = max(mc, cl[s[r]])
            if r - l + 1 > k + mc:
                cl[s[l]] -= 1
                l += 1
            ml = max(r-l+1, ml)
            r += 1
        return ml
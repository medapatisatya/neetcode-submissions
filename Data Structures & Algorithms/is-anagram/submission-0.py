class Solution:
    def count(self, string, dictionary=dict()):
        for ch in string:
            if ch in dictionary: dictionary[ch] += 1
            else: dictionary[ch] = 1
        return dictionary
    
    def checkAnagram(self, ss, ds):
        for key in ss:
            if key in ds and ss[key] == ds[key]:
                continue
            return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        # # Using hashMap (dict)
        sd, td = self.count(s, dict()), self.count(t, dict())
        return self.checkAnagram(sd, td) and self.checkAnagram(td, sd)

        # Using sorting
        # sd, td = sorted(s), sorted(t)
        # return sd == td



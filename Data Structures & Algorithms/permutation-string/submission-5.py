class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1

        
        window_count = {}

        l = 0
        for r in range(len(s2)):
            window_count[s2[r]] = window_count.get(s2[r], 0) + 1
            
            if r - l + 1 == len(s1):
                if window_count == s1_count:
                    return True
                window_count[s2[l]] -= 1
                if not window_count[s2[l]]:
                    del window_count[s2[l]]
                l += 1
        
        return False